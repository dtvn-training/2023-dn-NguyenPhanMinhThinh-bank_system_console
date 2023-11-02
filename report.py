from abc import ABC, abstractmethod

class Report():
    @abstractmethod
    def log(self, amount):
        pass
