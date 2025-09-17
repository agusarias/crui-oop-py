#Interfaz
class OpcionMenu:
    def mostrar(self, nivel=0):
        pass

#Hoja
class Item(OpcionMenu):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + "- " + self.nombre)

#El componente compuesto
class Menu(OpcionMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.opciones = []

    def agregar(self, opcion):
        self.opciones.append(opcion)

    def mostrar(self, nivel=0):
        print("  " * nivel + "+ " + self.nombre)
        for opcion in self.opciones:
            opcion.mostrar(nivel + 1)


if __name__ == "__main__":
    menu_principal = Menu("Productos")

    
    calzados = Menu("Calzados")
    calzados.agregar(Item("Botas"))
    calzados.agregar(Item("Sandalias"))

    
    ropa = Menu("Ropa")
    ropa.agregar(Item("Buzos"))
    ropa.agregar(Item("Camperas"))

    
    menu_principal.agregar(calzados)
    menu_principal.agregar(ropa)

    
    menu_principal.mostrar()