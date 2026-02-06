from machine import lightsleep, reset

from states.state import AbstractState
from utils import write_details
import utils.logging as logging

class Sleep(AbstractState):
    def exec(self) -> None:
        self.enter()

        self.device.light.change_color()

        if self.device.details.get('error'):
            del self.device.details['error']

        write_details(self.device.details)

        lightsleep(10 * 1000)

        self.exit()

    def enter(self) -> None:
        logging.debug('Entering Sleep state...')

    def exit(self) -> None:
        logging.debug('Exiting Sleep state...')
        reset()