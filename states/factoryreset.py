from machine import reset

from states.state import AbstractState
from utils import remove_settings
import utils.logging as logging

class FactoryReset(AbstractState):
    def exec(self) -> None:
        self.enter()

        remove_settings()

        self.exit()

    def enter(self) -> None:
        logging.debug('Entering Factory Reset state...')

    def exit(self) -> None:
        logging.debug('Exiting Factory Reset state...')
        reset()