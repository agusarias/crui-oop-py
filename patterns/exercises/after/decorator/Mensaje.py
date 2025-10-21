class Mensaje(ABC):
    @abstractmethod
    def get_contenido(self) -> str:
        pass