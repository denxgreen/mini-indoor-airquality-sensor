import json

from constants import DETAILS_FILE

def read_details() -> dict:
    with open(DETAILS_FILE, 'r') as file:
        details = json.load(file)
        return details

def write_details(details: dict) -> None:
    with open(DETAILS_FILE, 'w') as file:
        json.dump(details, file)