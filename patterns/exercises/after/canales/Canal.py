from abc import ABC, abstractmethod


class Canal(ABC):
    @abstractmethod
    def notificar(content:str):
        pass