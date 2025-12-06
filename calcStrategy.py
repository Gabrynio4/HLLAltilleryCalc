from abc import ABC, abstractmethod
from functools import wraps

class CalcStrategy(ABC):
    MIN_DISTANCE = 100
    MAX_DISTANCE = 1600

    def distance_check(method):
        @wraps(method)
        def wrapper(self, distance):
            if not (self.MIN_DISTANCE <= distance <= self.MAX_DISTANCE):
                return 0
            return method(self, distance)
        return wrapper
    
    @abstractmethod
    def calculate(self, distance: int) -> int:
        pass