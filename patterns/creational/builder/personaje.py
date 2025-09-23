class Personaje:
    def __init__(self, nombre, rol, elemento, via, planeta):
        self.nombre = nombre
        self.rol = rol
        self.elemento = elemento
        self.via = via
        self.planeta = planeta

    def __str__(self):
        return f"Nombre: {self.nombre}, Rol: {self.rol}, Elemento: {self.elemento}, Vía: {self.via}, Planeta: {self.planeta}"


#Aca definimos los atributos que tendra nuestro personaje, ya sea el nombre, el rol, elementos y demas, nos devolvera en forma de string