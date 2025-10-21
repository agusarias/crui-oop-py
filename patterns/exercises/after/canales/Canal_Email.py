import base64
from Canal import Canal

class Canal_Email(Canal):
    def notificar(content:str):
        print("Enviando por EMAIL...")
        print("Asunto: Nueva Notificación")
        # Decodificamos de Base64 para mostrar el cuerpo original
        cuerpo_decodificado = base64.b64decode(content).decode("utf-8")
        print(f"Cuerpo (decodificado): {cuerpo_decodificado}")
        print("Email enviado.\n")