from abc import ABC, abstractmethod

#every checks should have check()
    # True -> OK
    # False -> Failed

#with this, we'll be able to create database, config, aws, etc checks
class HealthCheck(ABC):

    @abstractmethod
    def check(self) -> bool:
        pass