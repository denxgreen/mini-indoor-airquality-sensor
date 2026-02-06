import json
import os

from constants import DATA_PATH, SETTINGS_FILE
from models import Settings
from utils.path import create_directory, directory_exists

def read_settings() -> Settings:
    with open(SETTINGS_FILE, 'r') as file:
        settings = json.load(file)
        return Settings(**settings)

def write_settings(settings: Settings) -> None:
    if not directory_exists(DATA_PATH):
        create_directory(DATA_PATH)

    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings.model_dump(), file)

def write_default_settings() -> None:
    if not directory_exists(DATA_PATH):
        create_directory(DATA_PATH)

    with open(SETTINGS_FILE, 'w') as file:
        default_settings = Settings()
        json.dump(default_settings.model_dump(), file)

def remove_settings() -> None:
    os.remove(SETTINGS_FILE)