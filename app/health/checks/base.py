from abc import ABC, abstractmethod

class HealthCheck(ABC):

    @abstractmethod
    def check(self) -> bool:
        pass