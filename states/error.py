from states.state import AbstractState
import utils.logging as logging

class Error(AbstractState):
    def exec(self) -> None:
        self.enter()
        
        self.exit()
    
    def enter(self) -> None:
        logging.debug('>>Entering Error state...')
        
    def exit(self) -> None:
        logging.debug('>>Exiting Error state...')
