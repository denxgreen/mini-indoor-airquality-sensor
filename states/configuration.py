from states.state import AbstractState
import utils.logging as logging

class Configuration(AbstractState):
    def exec(self) -> None:
        self.enter()
        
        self.exit()
    
    def enter(self) -> None:
        logging.debug('>>Entering Configuration state...')
        
    def exit(self) -> None:
        logging.debug('>>Exiting Configuration state...')