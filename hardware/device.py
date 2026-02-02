class Device:
    def __init__(self) -> None:
        self.state = None
        self.settings = None
        
    def run(self) -> None:
        while True:
            self.state.exec()