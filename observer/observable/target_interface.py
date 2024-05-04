from abc import ABC,abstractmethod
from typing import Any
from observer.observer_interface import ObserverInterface

class TargetInterface(ABC):
    @abstractmethod
    def add_observer(self,obs:ObserverInterface):
        pass

    def remove_observer(self,obs:ObserverInterface):
        pass

    def get_state(self):
        pass
    def set_state(self):
        pass

    def state_change(self):
        pass

