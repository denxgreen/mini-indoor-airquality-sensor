from machine import Pin

from constants import BUTTON_PIN, LIGHT_PIN
from hardware.actuators import Neopixel
from states.init import Init

class Device:
    def __init__(self) -> None:
        self.state = Init(self)
        self.settings = None
        self.details = dict()
        self.sensors = set()
        self.button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
        self.light = Neopixel(self, LIGHT_PIN, 1)

    def run(self) -> None:
        while True:
            self.state.exec()