from Mensaje import Mensaje

class MensajeMejorado(Mensaje):
    def __init__(self, mensaje_envuelto: Mensaje):
        self._mensaje_envuelto = mensaje_envuelto

    def get_contenido(self) -> str:
        return self._mensaje_envuelto.get_contenido()