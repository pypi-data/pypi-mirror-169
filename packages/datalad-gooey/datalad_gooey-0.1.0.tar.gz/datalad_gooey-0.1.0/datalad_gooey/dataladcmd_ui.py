from types import MappingProxyType
from typing import (
    Dict,
)
from PySide6.QtCore import (
    QObject,
    Signal,
    Slot,
)
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QLabel,
    QScrollArea,
    QWidget,
)

from .param_form_utils import populate_form_w_params
from .api_utils import get_cmd_displayname
from .active_suite import spec as active_suite


class GooeyDataladCmdUI(QObject):

    configured_dataladcmd = Signal(str, MappingProxyType)

    def __init__(self, app, ui_parent: QWidget):
        super().__init__()
        self._app = app
        self._ui_parent = ui_parent
        # start out disabled, there will be no populated form
        self._ui_parent.setDisabled(True)
        self._pform = None
        self._cmd_title = None

    @property
    def pwidget(self):
        return self._ui_parent

    @property
    def pform(self):
        if self._pform is None:
            pw = self.pwidget
            # make sure all expected UI blocks are present
            self._cmd_title = pw.findChild(QLabel, 'cmdTabTitle')
            scrollarea_content = pw.findChild(QScrollArea).widget()
            buttonbox = pw.findChild(QDialogButtonBox, 'cmdTabButtonBox')
            for w in (self._cmd_title, scrollarea_content, buttonbox):
                assert w
            # create main form layout for the parameters to appear in
            form_layout = QFormLayout(scrollarea_content)
            form_layout.setObjectName('cmdTabFormLayout')
            self._pform = form_layout

            # connect the dialog interaction with slots in this instance
            # we run the retrieval helper on ok/run
            buttonbox.accepted.connect(self._retrieve_input)
            # we disable the UI (however that might look like) on cancel
            buttonbox.rejected.connect(self.disable)
        return self._pform

    @Slot(str, dict)
    def configure(
            self,
            api=None,
            cmdname: str = None,
            cmdkwargs: Dict or None = None):
        if cmdkwargs is None:
            cmdkwargs = dict()

        # figure out the object that emitted the signal triggering
        # this slot execution. Will be None for a regular method call.
        # we can use this to update the method parameter values
        # with information from menu-items, or tree nodes clicked
        sender = self.sender()
        if sender is not None and isinstance(sender, QAction):
            if api is None:
                api = sender.data().get('__api__')
            if cmdname is None:
                cmdname = sender.data().get('__cmd_name__')
            # pull in any signal-provided kwargs for the command
            # unless they have been also specified directly to the method
            cmdkwargs = {
                k: v for k, v in sender.data().items()
                if k not in ('__cmd_name__', '__api__')
                and k not in cmdkwargs
            }

        assert cmdname is not None, \
            "GooeyDataladCmdUI.configure() called without command name"

        self._app.get_widget('contextTabs').setCurrentWidget(self.pwidget)

        self.reset_form()
        populate_form_w_params(
            api,
            self._app.rootpath,
            self.pform,
            cmdname,
            cmdkwargs,
        )
        # set title afterwards, form might just have been created first, lazily
        self._cmd_title.setText(
            # remove potential shortcut marker
            get_cmd_displayname(api, cmdname).replace('&', '')
        )
        self._cmd_title.setToolTip(f'API command: `{cmdname}`')
        # deposit the command name in the widget, to be retrieved later by
        # retrieve_parameters()
        self.pform.datalad_cmd_name = cmdname
        # make sure the UI is visible
        self.pwidget.setEnabled(True)

    @Slot()
    def _retrieve_input(self):
        from .param_widgets import _NoValue
        params = dict()
        for i in range(self.pform.rowCount()):
            # the things is wrapped into a QWidgetItem layout class, hence .wid
            field_widget = self.pform.itemAt(i, QFormLayout.FieldRole).wid
            # _get_datalad_param_spec() is our custom private adhoc method
            # expected to return a dict with a parameter setting, or an
            # empty dict, when the default shall be used.
            params.update({
                k: v for k, v in field_widget.get_gooey_param_spec().items()
                if v is not _NoValue
            })
        self.disable()
        self.configured_dataladcmd.emit(
            self.pform.datalad_cmd_name,
            MappingProxyType(params),
        )

    @Slot()
    def disable(self):
        """Disable UI when no longer needed for configuration"""
        # only disaable, not hide, to keep the info what ran (was configured)
        # accessible. Widget empties itself on reconfigure
        self.pwidget.setDisabled(True)

    def reset_form(self):
        if self._cmd_title:
            self._cmd_title.setText('')
        for i in range(self.pform.rowCount() - 1, -1, -1):
            # empty the form layout (deletes all widgets)
            self.pform.removeRow(i)
        self.disable()
