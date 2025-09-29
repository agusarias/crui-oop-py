from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def descripcion(self):
        pass

class Cafe(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    def descripcion(self):
        return f"Café {self.nombre} (${self.precio})"

class Te(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    def descripcion(self):
        return f"Té {self.nombre} (${self.precio})"

class PorcionTorta(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    def descripcion(self):
        return f"Porción de torta de {self.nombre} (${self.precio})"


class PorcionTortaDecorator(PorcionTorta):
    def __init__(self, porcion):
        self.porcion = porcion

    @abstractmethod
    def descripcion(self):
        pass

class ConLeche(PorcionTortaDecorator):
    def __init__(self, porcion):
        super().__init__(porcion)
        self.precio = porcion.precio + 20  

    def descripcion(self):
        return self.porcion.descripcion() + " + Leche extra"

class ConCrema(PorcionTortaDecorator):
    def __init__(self, porcion):
        super().__init__(porcion)
        self.precio = porcion.precio + 30  

    def descripcion(self):
        return self.porcion.descripcion() + " + Crema"

class ConDescuento(PorcionTortaDecorator):
    def __init__(self, porcion, porcentaje):
        super().__init__(porcion)
        self.precio = porcion.precio * (1 - porcentaje/100)
        self.porcentaje = porcentaje

    def descripcion(self):
        return self.porcion.descripcion() + f" (-{int(self.porcentaje)}% descuento)"