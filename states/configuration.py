from machine import reset
from time import sleep

from constants import DATA_PATH
from states.state import AbstractState
from utils import Color, write_default_settings, write_details
from utils.path import create_directory, directory_exists
import utils.logging as logging

class Configuration(AbstractState):
    def exec(self) -> None:
        self.enter()

        if not directory_exists(DATA_PATH):
            create_directory(DATA_PATH)

        write_default_settings()

        write_details(self.device.details)

        sleep(3)

        self.exit()

    def enter(self) -> None:
        logging.debug('Entering Configuration state...')
        self.device.light.change_color(Color.CYAN)

    def exit(self) -> None:
        logging.debug('Exiting Configuration state...')
        self.device.light.change_color(Color.OFF)
        reset()