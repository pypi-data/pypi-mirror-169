from pathlib import Path
from typing import Dict

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (
    QFile,
    QIODevice,
)


class _NoValue:
    """Type to annotate the absence of a value

    For example in a list of parameter defaults. In general `None` cannot
    be used, as it may be an actual value, hence we use a local, private
    type.
    """
    pass


def load_ui(name, parent=None):
    ui_file_name = Path(__file__).parent / 'resources' / 'ui' / f"{name}.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        raise RuntimeError(
            f"Cannot open {ui_file_name}: {ui_file.errorString()}")
    loader = QUiLoader()
    ui = loader.load(ui_file, parentWidget=parent)
    ui_file.close()
    if not ui:
        raise RuntimeError(
            f"Cannot load UI {ui_file_name}: {loader.errorString()}")
    return ui


def render_cmd_call(cmdname: str, cmdkwargs: Dict):
    """Minimalistic Python-like rendering of commands for the logs"""
    cmdkwargs = cmdkwargs.copy()
    ds_path = cmdkwargs.pop('dataset', None)
    if ds_path:
        if hasattr(ds_path, 'pathobj'):
            ds_path = ds_path.path
        ds_path = str(ds_path)
    # show commands running on datasets as dataset method calls
    rendered = "<b>Running:</b> "
    rendered += f"<code>Dataset({ds_path!r})." if ds_path else ''
    rendered += f"{cmdname}<nobr>("
    rendered += ', '.join(
        f"<i>{k}</i>={v!r}"
        for k, v in cmdkwargs.items()
        if k not in ('return_type', 'result_xfm')
    )
    rendered += ")</code>"
    return rendered
