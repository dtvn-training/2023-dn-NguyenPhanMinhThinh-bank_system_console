from abc import ABC, abstractmethod


class Withdraw(ABC):
    @abstractmethod
    def withdraw(self, amount) -> bool:
        pass

    @abstractmethod
    def isAccepted(self, amount) -> bool:
        pass
