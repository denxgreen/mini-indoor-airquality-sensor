class AbstractSensor:
    def __init__(self, device) -> None:
        self.device = device
        
    def get_measurements() -> dict:
        ...
    
    def check_measurements() -> bool:
        ...