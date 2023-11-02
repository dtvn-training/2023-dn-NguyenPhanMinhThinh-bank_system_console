from abc import ABC, abstractmethod

class Withdraw(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def isAccepted(self, amount):
        pass