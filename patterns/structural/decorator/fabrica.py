from productos import Cafe, Te, PorcionTorta

class FabricaProductos:
    @staticmethod
    def crear_producto(tipo, nombre, precio):
        if tipo == "cafe":
            return Cafe(nombre, precio)
        elif tipo == "te":
            return Te(nombre, precio)
        elif tipo == "torta":
            return PorcionTorta(nombre, precio)
        else:
            raise ValueError("Tipo de producto no válido")