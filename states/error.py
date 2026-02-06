from states.state import AbstractState
from states.sleep import Sleep
from utils import Color, ERROR_CODES
import utils.logging as logging

class Error(AbstractState):
    def __init__(self, device, error: Exception) -> None:
        super().__init__(device)
        self.error = error

    def exec(self) -> None:
        self.enter()

        self.device.details['error'] = ERROR_CODES.get(self.error.errno).get('message')

        self.device.light.blink(color=Color.RED, n=ERROR_CODES.get(self.error.errno).get('blinks_number'))

        self.exit()

    def enter(self) -> None:
        logging.debug('Entering Error state...')

    def exit(self) -> None:
        logging.debug('Exiting Error state...')
        self.device.state = Sleep(self.device)