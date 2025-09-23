from personaje import Personaje 

class Patron:
    def __init__(self):
        self.nombre = "Ninguno" 
        self.rol = "Ninguno"
        self.elemento = "Ninguno"
        self.via = "Ninguno"
        self.planeta = "Ninguno" 

    def set_nombre(self, nombre):
        self.nombre = nombre
        return self
    
    def set_rol(self, rol):
        self.rol = rol
        return self
    
    def set_elemento(self, elemento):
        self.elemento = elemento
        return self
    
    def set_via(self, via):
        self.via = via
        return self
    
    def set_planeta(self, planeta):
        self.planeta = planeta
        return self
    
    def build(self):
        return Personaje(self.nombre, self.rol, self.elemento, self.via, self.planeta)


#aca creamos el patron, donde le vamos a dar un valor en caso de no encontrar o eliminar un atributo principal, retornando su self (no se explicarlo bien xd)