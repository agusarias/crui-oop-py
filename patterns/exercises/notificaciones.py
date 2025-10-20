import base64
import sys
from abc import ABC, abstractmethod
from datetime import datetime

"""
Sistema de Envío de Notificaciones

Contestar a continuación las siguientes preguntas:

- Qué patrón de diseño podés identificar en el código dado?
- Qué patrones de diseño se podrían agregar para mejorar el código?
- Implementar uno o más de estos patrones adicionales para mejorar el código.
"""


class ConfigurationManager:
    """
    Gestiona la configuración global de la aplicación.
    """

    _instance = None

    def __init__(self):
        # El constructor no debería ser llamado directamente.
        raise RuntimeError("¡Llamar a get_instance() en su lugar!")

    @classmethod
    def get_instance(cls):
        """Obtiene la única instancia de la clase."""
        if cls._instance is None:
            # Crea la instancia si no existe.
            cls._instance = cls.__new__(cls)
            cls._instance.admin_name = "admin@sistema.com"
        return cls._instance

    def get_admin_name(self):
        return self.admin_name


class Mensaje(ABC):
    @abstractmethod
    def get_contenido(self) -> str:
        pass


class MensajeSimple(Mensaje):
    def __init__(self, texto: str):
        self._texto = texto

    def get_contenido(self) -> str:
        return self._texto


class MensajeMejorado(Mensaje):
    def __init__(self, mensaje_envuelto: Mensaje):
        self._mensaje_envuelto = mensaje_envuelto

    def get_contenido(self) -> str:
        return self._mensaje_envuelto.get_contenido()


class MensajeUrgente(MensajeMejorado):
    def get_contenido(self) -> str:
        return f"[URGENTE] {super().get_contenido()}"


class MensajeConTimestamp(MensajeMejorado):
    def get_contenido(self) -> str:
        timestamp = datetime.now().isoformat()
        return f"({timestamp}) {super().get_contenido()}"


class MensajeEnBase64(MensajeMejorado):
    def get_contenido(self) -> str:
        contenido_original = super().get_contenido()
        return base64.b64encode(contenido_original.encode("utf-8")).decode("utf-8")


class EnviadorDeMensajes:
    """
    Esta clase es responsable de enviar mensajes
    """

    def enviar(self, mensaje: Mensaje, canal: str):
        contenido = mensaje.get_contenido()
        canal = canal.upper()

        if canal == "EMAIL":
            print("Enviando por EMAIL...")
            print("Asunto: Nueva Notificación")
            # Decodificamos de Base64 para mostrar el cuerpo original
            cuerpo_decodificado = base64.b64decode(contenido).decode("utf-8")
            print(f"Cuerpo (decodificado): {cuerpo_decodificado}")
            print("Email enviado.\n")
        elif canal == "SMS":
            print("Enviando por SMS...")
            # Limita a 160 caracteres
            print(f"Mensaje: {contenido[:160]}")
            print("SMS enviado.\n")
        elif canal == "PUSH":
            print("Enviando Notificación PUSH...")
            print(f'Payload: {{ "content": "{contenido}" }}')
            print("Push enviada.\n")
        else:
            print(f"Error: El canal '{canal}' no es soportado.\n", file=sys.stderr)


# =================================================================
# Punto de entrada principal de la aplicación
# =================================================================

if __name__ == "__main__":
    config = ConfigurationManager.get_instance()
    print(f"Sistema configurado por: {config.get_admin_name()}")
    print("------------------------------------------")

    mi_mensaje = MensajeSimple("Este es el cuerpo del mensaje principal.")
    mi_mensaje = MensajeConTimestamp(mi_mensaje)
    mi_mensaje = MensajeUrgente(mi_mensaje)
    mi_mensaje = MensajeEnBase64(mi_mensaje)  # Codifica el contenido final

    contenido_final = mi_mensaje.get_contenido()
    print("Mensaje formateado listo para enviar:")
    print(contenido_final)
    print("------------------------------------------")

    # 3. Enviamos el mensaje por diferentes canales.
    enviador = EnviadorDeMensajes()
    enviador.enviar(mi_mensaje, "EMAIL")
    enviador.enviar(mi_mensaje, "SMS")
    enviador.enviar(mi_mensaje, "PUSH")
