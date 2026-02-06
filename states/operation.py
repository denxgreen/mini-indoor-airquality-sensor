from time import sleep

from states.state import AbstractState
from states.error import Error
from states.sleep import Sleep
from utils import Color, write_measurements
import utils.logging as logging

class Operation(AbstractState):
    def exec(self) -> None:
        self.enter()

        measurements = dict()

        for sensor in self.device.sensors:
            sleep(1)
            try:
                measurements |= sensor.get_measurements()
            except OSError as error:
                self.device.state = Error(self.device, error)
                return

        write_measurements(measurements)

        self.exit()

    def enter(self) -> None:
        logging.debug('Entering Operation state...')
        self.device.light.change_color(Color.GREEN)

    def exit(self) -> None:
        logging.debug('Exiting Operation state...')
        self.device.state = Sleep(self.device)