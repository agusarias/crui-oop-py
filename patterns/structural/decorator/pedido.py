class Pedido:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto):
        self.items.append(producto)

    def mostrar_pedido(self):
        print("\n--- Pedido actual ---")
        total = 0
        for p in self.items:
            print(p.descripcion())
            total += p.precio
        print(f"Total a pagar: ${total}")
        return total