import os

def file_exists(path: str) -> bool:
    try:
        with open(path, 'r') as file:
            return True
    except OSError:
        return False

def directory_exists(name: str) -> bool:
    directories = os.listdir()

    if name.strip('/') not in directories:
        return False

    return True

def create_directory(name: str) -> None:
    os.mkdir(os.getcwd() + name)

def remove_directory(name: str) -> None:
    os.rmdir(os.getcwd() + name)