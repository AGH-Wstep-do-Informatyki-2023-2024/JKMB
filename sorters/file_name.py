import os
show_name = "Po nazwie"
def sort(files: list[str]):
    new_dir_structure = {}
    new_dir_structure[""] = sorted(files, key=str.lower)
    return new_dir_structure
