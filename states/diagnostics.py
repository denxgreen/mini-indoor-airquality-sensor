from states.state import AbstractState
import utils.logging as logging

class Diagnostics(AbstractState):
    def exec(self) -> None:
        self.enter()
        
        self.exit()
    
    def enter(self) -> None:
        logging.debug('>>Entering Diagnostics state...')
        
    def exit(self) -> None:
        logging.debug('>>Exiting Diagnostics state...')