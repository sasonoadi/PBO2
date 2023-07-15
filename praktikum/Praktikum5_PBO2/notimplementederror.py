from abc import ABC, abstractmethod

class BaseDog(ABC):

    @abstractmethod
    def how(self):
        raise NotImplementedError("Subclasses should implement this!")