from MensajeMejorado import MensajeMejorado

class MensajeUrgente(MensajeMejorado):
    def get_contenido(self) -> str:
        return f"[URGENTE] {super().get_contenido()}"