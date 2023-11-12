import os
from pathlib import Path


def get_project_root() -> Path:
    """
    Returns the project root, useful for getting absolute paths in other files.

    Returns
    -------
    The project root.
    """
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent
    return project_root


def go_to_root_folder() -> None:
    """
    Goes to the root folder, useful for accessing data folder simply in notebooks.

    Returns
    -------
    None
    """
    os.chdir(get_project_root())
