from sensors.sensor import AbstractSensor

class THSensor(AbstractSensor):
    def __init__(self, device, pin: int) -> None:
        super.__init__(device)
    
    def get_measurements() -> dict:
        ...
        
    def check_measurements() -> bool:
        ...