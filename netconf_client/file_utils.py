import os

DEFAULT_FILTER_DIR = 'filters'

def read_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read()

def get_file(file: str) -> str:
    if find_if_abs_path_was_provided(file):
        return file
    return path_to_script_execution(file)

def find_if_abs_path_was_provided(file: str): 
    return path_exists(file) and file_exists(file)

def path_exists(file: str) -> bool:
    return os.path.exists(file)

def file_exists(file: str) -> bool:
    return os.path.isfile(file)

def path_to_script_execution(file: str) -> str:
    return f'{real_path(abs_path(__file__))}/{file}'

def real_path(path: str) -> str:
    return os.path.realpath(path)

def abs_path(path: str) -> str:
    return os.path.abspath(os.path.dirname(path))


def find_filter_path(file: str) -> str:
    if find_if_abs_path_was_provided(file):
        return file
    return use_default_working_dir(file)

def use_default_working_dir(file: str) -> str: 
    return f'{real_path(abs_path(__file__))}/{DEFAULT_FILTER_DIR}/{file}'


def remove_path(file: str) -> str:
    return os.path.basename(file)