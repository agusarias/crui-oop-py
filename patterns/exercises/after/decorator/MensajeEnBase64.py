from MensajeMejorado import MensajeMejorado
import base64

class MensajeEnBase64(MensajeMejorado):
    def get_contenido(self) -> str:
        contenido_original = super().get_contenido()
        return base64.b64encode(contenido_original.encode("utf-8")).decode("utf-8")