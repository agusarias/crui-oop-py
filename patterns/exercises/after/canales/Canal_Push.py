from Canal import Canal

class Canal_Push(Canal):
    def notificar(content:str):
        print("Enviando Notificación PUSH...")
        print(f'Payload: {{ "content": "{content}" }}')
        print("Push enviada.\n")