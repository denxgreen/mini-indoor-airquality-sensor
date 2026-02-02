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
        formatted_settings = json.dumps(settings.model_dump())
        json.dump(formatted_settings, file)
        
def write_default_settings() -> None:
    with open(SETTINGS_FILE, 'w') as file:
        default_settings = Settings()
        formatted_default_settings = json.dumps(default_settings.model_dump())
        json.dump(formatted_default_settings, file)
        
def remove_settings() -> None:
    os.remove(SETTINGS_FILE)