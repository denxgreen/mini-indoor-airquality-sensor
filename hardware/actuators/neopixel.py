from neopixel import NeoPixel
from time import sleep

from hardware.actuators.light import AbstractLight
from utils import Color

class Neopixel(AbstractLight):
    def __init__(self, device, pin: int, leds_number: int) -> None:
        super().__init__(device, pin)
        self.neopixel = NeoPixel(self.pin, leds_number)

    def change_color(self, color: tuple = Color.OFF) -> None:
        self.neopixel.fill(color)
        self.neopixel.write()

    def blink(self, color: tuple, sec: float = 0.35, n=1) -> None:
        for _ in range(n):
            self.change_color(color)
            sleep(sec)
            self.change_color()
            sleep(sec)