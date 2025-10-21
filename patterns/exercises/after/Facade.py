from .decorator import *

class Facade:

    @classmethod
    def formatearMensaje(msg:str)->MensajeMejorado:
        mi_mensaje = MensajeSimple(msg)
        mi_mensaje = MensajeConTimestamp(mi_mensaje)
        mi_mensaje = MensajeUrgente(mi_mensaje)
        mi_mensaje = MensajeEnBase64(mi_mensaje)  # Codifica el contenido final

        return mi_mensaje