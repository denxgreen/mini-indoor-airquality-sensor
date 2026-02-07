class AbstractState:
    def __init__(self, device) -> None:
        self.device = device
        
    def exec(self) -> None:
        ...
    
    def enter(self) -> None:
        ...
        
    def exit(self) -> None:
        ...