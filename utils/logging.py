import os

from constants import LOGS_PATH
from utils.path import create_directory, directory_exists, file_exists

DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3
CRITICAL = 4

class Config:
    level: int = DEBUG
    filename: str = ""

    def __init__(self, level: int = DEBUG, filename: str = "") -> None:
        Config.level = level
        Config.filename = filename

        if file_exists(LOGS_PATH + Config.filename):
            os.remove(LOGS_PATH + Config.filename)

def log(content: str, level_name: str, level_value: int) -> None:
    if level_value >= Config.level:
        if Config.filename:
            if not directory_exists(LOGS_PATH):
                create_directory(LOGS_PATH)

            with open(LOGS_PATH + Config.filename, 'a') as file:
                file.write(f'{level_name} - {content}\n')
        else:
            print(f'{level_name} - {content}')

def debug(content: str) -> None:
    log(content, 'DEBUG', DEBUG)

def info(content: str) -> None:
    log(content, 'INFO', INFO)

def warning(content: str) -> None:
    log(content, 'WARNING', WARNING)

def error(content: str) -> None:
    log(content, 'ERROR', ERROR)

def critical(content: str) -> None:
    log(content, 'CRITICAL', CRITICAL)