from states.state import AbstractState
import utils.logging as logging

class Sleep(AbstractState):
    def exec(self) -> None:
        self.enter()
        
        self.exit()
    
    def enter(self) -> None:
        logging.debug('>>Entering Sleep state...')
        
    def exit(self) -> None:
        logging.debug('>>Exiting Sleep state...')
