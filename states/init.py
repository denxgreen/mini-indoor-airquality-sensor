from time import sleep

from hardware.sensors import DHT
from states.state import AbstractState
from states.configuration import Configuration
from states.factoryreset import FactoryReset
from states.diagnostics import Diagnostics
from utils import Color, SettingsError, read_settings, read_details
import constants as const
import utils.logging as logging

class Init(AbstractState):
    def exec(self) -> None:
        self.enter()

        try:
            self.device.settings = read_settings()
            self.device.details = read_details()
            self.device.sensors.add(DHT(self.device, const.THSENSOR_PIN))
        except (OSError, SettingsError) as error:
            logging.error(error)
            self.device.state = Configuration(self.device)
            return

        sleep(3)

        button_pressed_duration = 0
        while self.device.button.value() == 0:
            button_pressed_duration += 1

            if const.SHORT_PRESS_DURATION <= button_pressed_duration < const.LONG_PRESS_DURATION:
                self.device.light.change_color(Color.CYAN)
                self.device.state = Configuration(self.device)
            elif button_pressed_duration >= const.LONG_PRESS_DURATION:
                self.device.light.change_color(Color.ORANGE)
                self.device.state = FactoryReset(self.device)

            sleep(1)

        if button_pressed_duration >= const.SHORT_PRESS_DURATION:
            return

        self.exit()

    def enter(self) -> None:
        logging.debug('Entering Init state...')

    def exit(self) -> None:
        logging.debug('Exiting Init state...')
        self.device.state = Diagnostics(self.device)