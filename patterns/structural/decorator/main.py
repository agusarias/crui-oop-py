from fabrica import FabricaProductos
from pedido import Pedido
from productos import ConLeche, ConCrema, ConDescuento

def main():
    pedido = Pedido()
    print("Bienvenido a la Sharktech Cofee ")
    
    while True:
        print("\nMenú:")
        print("1. Agregar Café")
        print("2. Agregar Té")
        print("3. Agregar Porcion de Torta")
        print("4. Ver pedido")
        print("5. Finalizar")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Tipo de café (Latte, Espresso...): ")
            precio = float(input("Precio: "))
            producto = FabricaProductos.crear_producto("cafe", nombre, precio)

            
            extra = input("¿Desea agregar leche extra (s/n)? ")
            if extra.lower() == "s":
                producto = ConLeche(producto)
            
            extra = input("¿Desea agregar crema (s/n)? ")
            if extra.lower() == "s":
                producto = ConCrema(producto)

            extra = input("¿Aplicar 10% de descuento (s/n)? ")
            if extra.lower() == "s":
                producto = ConDescuento(producto, 10)

            pedido.agregar_producto(producto)
        
        elif opcion == "2":
            nombre = input("Tipo de té (Verde, Negro...): ")
            precio = float(input("Precio: "))
            pedido.agregar_producto(FabricaProductos.crear_producto("te", nombre, precio))
        
        elif opcion == "3":
            nombre = input("Tipo de torta (Chocolate, Frutilla...): ")
            precio = float(input("Precio: "))
            pedido.agregar_producto(FabricaProductos.crear_producto("torta", nombre, precio))
        
        elif opcion == "4":
            pedido.mostrar_pedido()
        
        elif opcion == "5":
            print("\nGracias por tu compra Sharktech Cofee")
            pedido.mostrar_pedido()
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()