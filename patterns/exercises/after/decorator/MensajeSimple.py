from Mensaje import Mensaje

class MensajeSimple(Mensaje):
    def __init__(self, texto: str):
        self._texto = texto

    def get_contenido(self) -> str:
        return self._texto