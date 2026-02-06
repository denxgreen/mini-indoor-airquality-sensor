import json

from constants import DATA_PATH, DETAILS_FILE
from utils.path import create_directory, directory_exists

def read_details() -> dict:
    with open(DETAILS_FILE, 'r') as file:
        details = json.load(file)
        return details

def write_details(details: dict) -> None:
    if not directory_exists(DATA_PATH):
        create_directory(DATA_PATH)

    with open(DETAILS_FILE, 'w') as file:
        json.dump(details, file)