"""
# FileBrowser

Browse file (and directories) at the server side.

There are two modes possible

   * `can_select=False`
      * `on_file_open`: Triggered when **single** clicking a file or directoy.
      * `on_path_select`: Never triggered
      * `on_directory_change`: Triggered when clicking a directory
   * `can_select=True`
      * `on_file_open`: Triggered when **double** clicking a file or directoy.
      * `on_path_select`: Triggered when clicking a file or directoy
      * `on_directory_change`: Triggered when double clicking a directory

"""
from pathlib import Path
from typing import Optional, cast

from solara.alias import reacton, sol


@reacton.component
def Page():
    file, set_file = reacton.use_state(cast(Optional[Path], None))
    path, set_path = reacton.use_state(cast(Optional[Path], None))
    directory, set_directory = reacton.use_state(Path("~").expanduser())

    with sol.VBox() as main:
        can_select = sol.ui_checkbox("Enable select")

        def reset_path():
            set_path(None)
            set_file(None)

        # reset path and file when can_select changes
        reacton.use_memo(reset_path, [can_select])
        sol.FileBrowser(directory, on_directory_change=set_directory, on_path_select=set_path, on_file_open=set_file, can_select=can_select)
        sol.Info(f"You are in directory: {directory}")
        sol.Info(f"You selected path: {path}")
        sol.Info(f"You opened file: {file}")
    return main
