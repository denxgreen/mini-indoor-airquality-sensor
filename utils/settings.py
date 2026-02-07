import json
import os

from constants import SETTINGS_FILE
from models import Settings

def read_settings() -> Settings:
    with open(SETTINGS_FILE, 'r') as file:
        settings = json.load(file)
        return Settings(**settings)

def write_settings(settings: Settings) -> None:
    with open(SETTINGS_FILE, 'w') as file:
        json.dump(settings.model_dump(), file)

def write_default_settings() -> None:
    with open(SETTINGS_FILE, 'w') as file:
        default_settings = Settings()
        json.dump(default_settings.model_dump(), file)

def remove_settings() -> None:
    os.remove(SETTINGS_FILE)