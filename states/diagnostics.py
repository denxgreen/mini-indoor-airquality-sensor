from time import sleep

from states.state import AbstractState
from states.error import Error
from states.operation import Operation
from utils import Color, DiagnosticsError
import utils.logging as logging

class Diagnostics(AbstractState):
    def exec(self) -> None:
        self.enter()

        for sensor in self.device.sensors:
            sleep(1)
            try:
                if not sensor.check_measurements():
                    error = DiagnosticsError()
                    logging.error(error)
                    self.device.state = Error(self.device, error)
                    return
            except OSError as error:
                logging.error(error)
                self.device.state = Error(self.device, error)
                return

        sleep(3)

        self.exit()

    def enter(self) -> None:
        logging.debug('Entering Diagnostics state...')
        self.device.light.change_color(Color.YELLOW)

    def exit(self) -> None:
        logging.debug('Exiting Diagnostics state...')
        self.device.state = Operation(self.device)