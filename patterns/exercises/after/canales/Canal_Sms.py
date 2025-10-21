from Canal import Canal

class Canal_Sms(Canal):
        def notificar(content:str):
            print("Enviando por SMS...")
            # Limita a 160 caracteres
            print(f"Mensaje: {content[:160]}")
            print("SMS enviado.\n")