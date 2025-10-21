from ConfigurationManager import ConfigurationManager
from .canales import *
from .decorator import MensajeMejorado
from EnviadorDeMensajes import EnviadorDeMensajes
from Facade import Facade

# =================================================================
# Punto de entrada principal de la aplicación
# =================================================================

if __name__ == "__main__":
    config = ConfigurationManager.get_instance()
    print(f"Sistema configurado por: {config.get_admin_name()}")
    print("------------------------------------------")

    mi_mensaje:MensajeMejorado = Facade.formatearMensaje("Este es el cuerpo del mensaje principal.")

    contenido_final = mi_mensaje.get_contenido()
    print("Mensaje formateado listo para enviar:")
    print(contenido_final)
    print("------------------------------------------")

    # 3. Enviamos el mensaje por diferentes canales.
    enviador = EnviadorDeMensajes()

    enviador.new_canal(Canal_Sms())
    enviador.new_canal(Canal_Email())
    enviador.new_canal(Canal_Push())
    
    enviador.enviar(mi_mensaje)
