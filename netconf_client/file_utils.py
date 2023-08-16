import os

DEFAULT_DEVICES_DIR = "devices"
DEFAULT_FILTER_DIR = "filters"


def read_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def write_to_file(file, text) -> str:
    with open(file, "a") as f:
        return f.write(text)


def find_devices_path(file: str) -> str:
    if find_if_abs_path_was_provided(file):
        return file
    return default_devices_working_dir(file)


def find_if_abs_path_was_provided(file: str):
    return path_exists(file) and file_exists(file)


def path_exists(file: str) -> bool:
    return os.path.exists(file)


def file_exists(file: str) -> bool:
    return os.path.isfile(file)


def default_devices_working_dir(file: str) -> str:
    return f"{real_path(abs_path(__file__))}/{DEFAULT_DEVICES_DIR}/{file}"


def real_path(path: str) -> str:
    return os.path.realpath(path)


def abs_path(path: str) -> str:
    return os.path.abspath(os.path.dirname(path))


def find_filter_path(file: str) -> str:
    if find_if_abs_path_was_provided(file):
        return file
    return default_filter_working_dir(file)


def default_filter_working_dir(file: str) -> str:
    return f"{real_path(abs_path(__file__))}/{DEFAULT_FILTER_DIR}/{file}"


def remove_path(file: str) -> str:
    # in the case of xpath, don't remove the namespace. For Cisco starts with http://
    if "http://" or "https://" in file:
        return file
    return os.path.basename(file)
