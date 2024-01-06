import puremagic, os

show_name = "Po typie pliku"


def sort(files: list[str]):
    new_dir_structure = {}
    for file in files:
        category = "unknown"
        if os.path.getsize(file) == 0:
            category = "empty"
        else:
            file_info = puremagic.magic_file(file)
            if len(file_info) > 0:
                category = file_info[0].mime_type.split("/")[0]
        if category not in new_dir_structure:
            new_dir_structure[category] = []
        new_dir_structure[category].append(file)

    return new_dir_structure
