from states.state import AbstractState
import utils.logging as logging

class Operation(AbstractState):
    def exec(self) -> None:
        self.enter()
        
        self.exit()
    
    def enter(self) -> None:
        logging.debug('>>Entering Operation state...')
        
    def exit(self) -> None:
        logging.debug('>>Exiting Operation state...')