from machine import reset
from time import sleep

from states.state import AbstractState
from utils import Color, write_default_settings, write_details
import utils.logging as logging

class Configuration(AbstractState):
    def exec(self) -> None:
        self.enter()

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