from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def log(self, amount):
        pass
