class AbstractSensor:
    def __init__(self, device) -> None:
        self.device = device

    def get_measurements(self) -> dict:
        ...

    def check_measurements(self) -> bool:
        ...