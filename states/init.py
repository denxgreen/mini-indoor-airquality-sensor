from states.state import AbstractState
import utils.logging as logging

class Init(AbstractState):
    def exec(self) -> None:
        self.enter()
        
        self.exit()
    
    def enter(self) -> None:
        logging.debug('>>Entering Init state...')
        
    def exit(self) -> None:
        logging.debug('>>Exiting Init state...')