import os


def create_folders(path_str: str | os.PathLike[str]) -> None:
    """
    Function for creating all folders for path
    @param path_str: Path
    """
    os.makedirs(os.path.split(path_str)[0], exist_ok=True)


def walk(folder: str | os.PathLike[str], base_path: str = '') -> list[str]:
    """
    Function for getting list of all files in folder and subfolders
    @param folder: Folder path str
    @param base_path: Prefix for path (for recursion)
    @return: list of files in folder and subfolders
    """
    def check_path(path):
        if len(path) > 0 and path[-1] != '/':
            path += '/'
        return path

    files = []

    folder = check_path(folder)
    base_path = check_path(base_path)

    for f in os.listdir(folder):
        if os.path.isdir(folder + f):
            files += walk(folder + f + '/', base_path + f + '/')
        else:
            files.append(base_path + f)
    return files


def get_filename_and_extension(file: str | os.PathLike[str]) -> tuple[str, [str | None]]:
    """
    Parse filename
    @param file: Path to file
    @return: tuple (filename, extension)
    """
    parts = file.rsplit('.', 2)

    return parts[0], parts[1] if len(parts) > 1 else None

