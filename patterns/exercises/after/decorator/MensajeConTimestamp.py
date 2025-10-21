from MensajeMejorado import MensajeMejorado
import datetime

class MensajeConTimestamp(MensajeMejorado):
    def get_contenido(self) -> str:
        timestamp = datetime.now().isoformat()
        return f"({timestamp}) {super().get_contenido()}"