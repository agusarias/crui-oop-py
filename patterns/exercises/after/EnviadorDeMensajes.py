from .decorator.Mensaje import Mensaje
import base64
import sys
from canales.Canal import Canal

class EnviadorDeMensajes:
    """
    Esta clase es responsable de enviar mensajes
    """
    _canals:list[Canal] = []

    def new_canal (self, canal:Canal):
        self._canals.append(canal)

    def enviar(self, mensaje: Mensaje):
        contenido = mensaje.get_contenido()

        for canal in self._canals:
            try:
                canal.notificar(contenido)

            except Exception:
                    print(f"Error: El canal '{canal}' no es soportado.\n", file=sys.stderr)