Getting started
###############

In order to start up ``DataLad Gooey``, double-click the program's icon on your Desktop or in your Explorer if you are on Windows, or find it in your Applications folder if you are on Mac.

An initial dialog let's you select a root directory.
Navigate to any directory you would like to open up, select it, and click ``Select Folder``.

.. image:: _static/start_location_selection.png

If you ``Cancel`` this dialog, the DataLad Gooey will open your home directory.

UI Overview
-----------

In general, the DataLad Gooey interface has three main sections: A tree view on the upper left, command pane on the upper right, and the log views at the bottom.

.. image:: _static/gooey_interface.png

The tree view should display files and directories on your computer, starting from the root directory picked at start up.
Double-clicking directories allows you to expand their contents, and to navigate into directory hierarchies.
You will notice that the ``Type`` and ``State`` annotations next to the file and directory names reveal details about files and directories:
You can distinguish directories and DataLad datasets and files.
Within datasets, files are either ``annexed-file``'s or ``file``'s, depending on how these files are tracked in the dataset.
The ``State`` property indicates the version-state of files, datasets, or directories: A new file, for example, would be annotated with an ``untracked`` state, a directory with a newly added unsaved change would be ``modified``, and neatly saved content would be annotated with a ``clean`` tag.


There are two ways of running DataLad command: either through the ``Dataset`` menu at the top, or by right-clicking on files, directories, or datasets in the tree view.
The latter option might be simpler to use, as it only allows commands suitable for the item that was right-clicked on, and prefills many parameter specifications.
The screenshot below shows the right-click context menu of a directory.

.. image:: _static/directory_menu.png


Once a DataLad command is selected, the ``Command`` tab contains relevant parameters and configurations for it.
The parameters will differ for each command, but hovering over their submenus or editors will show useful hints what to set them to.

.. image:: _static/command_pane_filled.png

The View Tab
^^^^^^^^^^^^

The ``View`` tab contains two submenus that allow you to alter the appearance of the interface.
Whenever you change the appearance of the interface, you need to close and reopen the program in order to let the change take effect.

The ``Theme`` submenu lets you switch between a light, dark, and system theme.

.. image:: _static/theme_menu.png

The ``Suite`` submenu lets you switch between suites that alter the command selection.
The two suites you will always be able to select between is a "simplified" command set, reduced to the most essential commands and parameters, and a "complete" command set.
DataLad extensions can add additional suites when you install them.
Please note that we recommend the "simplified" command suite to users, as the complete suite can contain experimental implementations.

.. image:: _static/suite_menu.png