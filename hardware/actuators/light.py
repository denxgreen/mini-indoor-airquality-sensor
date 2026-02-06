from machine import Pin

from utils import Color

class AbstractLight:
    def __init__(self, device, pin: int) -> None:
        self.device = device
        self.pin = Pin(pin, Pin.OUT)

    def change_color(self, color: tuple = Color.OFF) -> None:
        ...

    def blink(self, color: tuple, sec: float = 0.35, n: int = 1) -> None:
        ...