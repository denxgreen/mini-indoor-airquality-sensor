from states.state import AbstractState
import utils.logging as logging

class FactoryReset(AbstractState):
    def exec(self) -> None:
        self.enter()
        
        self.exit()
    
    def enter(self) -> None:
        logging.debug('>>Entering Factory Reset state...')
        
    def exit(self) -> None:
        logging.debug('>>Exiting Factory Reset state...')