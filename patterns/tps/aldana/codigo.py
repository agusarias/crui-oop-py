from typing import List

#/** * Contestar a continuación las siguientes preguntas: - Qué patrón de diseño podés identificar en el * código dado? - 
# Qué patrón de diseño podrías agregar para mejorar el código? *
# ===================== Dominio =====================

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class Carrito:
    def __init__(self):
        self.items: List[Producto] = []

    def add(self, producto: Producto):
        self.items.append(producto)

    def get_items(self):
        return self.items.copy()

    def subtotal(self):
        return sum(p.precio for p in self.items)

    def __str__(self):
        return str([str(p) for p in self.items])


#este 

# ===================== Observer =====================

class OrdenEventListener:
    def on_paid(self, orden):
        raise NotImplementedError


class EmailListener(OrdenEventListener):
    def on_paid(self, orden):
        print(f"[Email] Enviando comprobante a cliente. Total: ${orden.total()}")


class AnalyticsListener(OrdenEventListener):
    def on_paid(self, orden):
        print(f"[Analytics] Registrando venta. Ítems: {len(orden.carrito.get_items())}")


# ===================== Strategy (Medio de Pago) =====================

class MedioDePago:
    def pay(self, amount: float) -> bool:
        raise NotImplementedError


class PagoEfectivo(MedioDePago):
    def pay(self, amount: float) -> bool:
        print(f"[Cash] Recibidos ${amount} en efectivo.")
        return True


class PagoTarjeta(MedioDePago):
    def __init__(self, holder: str, card_number: str):
        self.holder = holder
        self.card_number = card_number

    def pay(self, amount: float) -> bool:
        print(f"[Card] Autorizando tarjeta de {self.holder} ****{self.last4()}")
        return amount <= 100.0

    def last4(self):
        return self.card_number[-4:] if self.card_number and len(self.card_number) >= 4 else "????"


# API externa simulada
class MercadoPagoAPI:
    def run_payment(self, amount_in_cents: int) -> bool:
        print(f"[MercadoPagoAPI] Procesando {amount_in_cents} centavos...")
        return amount_in_cents <= 15000


# ===================== Orden =====================

class Orden:
    def __init__(self, carrito: Carrito):
        self.carrito = carrito
        self.listeners: List[OrdenEventListener] = []
        self.payment_gateway: MedioDePago = None
        self.envoltorio_regalo = False
        self.envio_express = False

    def add_listener(self, listener: OrdenEventListener):
        self.listeners.append(listener)

    def set_medio_de_pago(self, medio: MedioDePago):
        self.payment_gateway = medio

    def incluir_envoltorio(self, valor: bool):
        self.envoltorio_regalo = valor

    def incluir_envio_express(self, valor: bool):
        self.envio_express = valor

    def total(self) -> float:
        total = self.carrito.subtotal()
        if self.envoltorio_regalo:
            total += 5.0
        if self.envio_express:
            total += 10.0
        return total

    def print_summary(self):
        print("=== ORDER SUMMARY ===")
        print(f"Items: {self.carrito}")
        print(f"Subtotal: ${self.carrito.subtotal()}")
        print(f"Envoltorio regalo: {'Si (+$5)' if self.envoltorio_regalo else 'No'}")
        print(f"Envio express: {'Si (+$10)' if self.envio_express else 'No'}")
        print(f"TOTAL: ${self.total()}")

    def pagar(self):
        if self.payment_gateway is None:
            print("No hay gateway de pago configurado.")
            return

        ok = self.payment_gateway.pay(self.total())
        if ok:
            print(f"Pago exitoso por ${self.total()}")
            self.notify_paid()
        else:
            print("Pago rechazado.")

    def notify_paid(self):
        for listener in self.listeners:
            listener.on_paid(self)


#Es un patron Strategy porque te permite poner cada clase separada en este caso los pagos 


# ===================== Main =====================
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

class Carrito:
    def __init__(self):
        self.items = []

    def add(self, producto):
        self.items.append(producto)

    def subtotal(self):
        return sum(p.precio for p in self.items)

    def __str__(self):
        return ', '.join(str(p) for p in self.items)

class OrdenBase:
    def __init__(self, carrito):
        self.carrito = carrito

    def total(self):
        return self.carrito.subtotal()

    def print_summary(self):
        print(f"Items: {self.carrito}")
        print(f"Subtotal: ${self.carrito.subtotal()}")

class OrdenDecorator(OrdenBase):
    def __init__(self, orden):
        self.orden = orden

    def total(self):
        return self.orden.total()

    def print_summary(self):
        self.orden.print_summary()

class Envoltorio(OrdenDecorator):
    def total(self):
        return super().total() + 5

    def print_summary(self):
        super().print_summary()
        print("Envoltorio regalo: si (+$5)")

class EnvioExpress(OrdenDecorator):
    def total(self):
        return super().total() + 10

    def print_summary(self):
        super().print_summary()
        print("Envio express: si (+$10)")

class MedioDePago:
    def pay(self):
        raise NotImplementedError

class PagoTarjeta(MedioDePago):
    def __init__(self, nombre, tarjeta):
        self.nombre = nombre
        self.tarjeta = tarjeta

    def pay(self, amount):
        print(f"Pagado ${amount} con tarjeta: {self.nombre} ****{self.tarjeta[-4:]}")
        return amount <= 100

class PagoEfectivo(MedioDePago):
    def pay(self, amount):
        print(f"Pagado ${amount} en efectivo")
        return True

if __name__ == "__main__":
    carrito = Carrito()
    carrito.add(Producto("Clean Code", 25))
    carrito.add(Producto("Mouse USB", 12.5))

    orden = EnvioExpress(Envoltorio(OrdenBase(carrito)))

    medio_de_pago = PagoTarjeta("Juan Perez", "4111111111111111")

    orden.print_summary()
    total = orden.total()

    if medio_de_pago.pay(total):
        print(f"Pago realizado: ${total}")
    else:
        print("Pago rechazado xD")


#se agrega decorador para hacer mas felxible o cambiar cosas sina fectar el codigo envolviendolos en wrappes 
#se puede hacer mejor 

   

#if __name__ == "__main__":
    # Productos base
    #libro = Producto("Clean Code", 25.0)
    #mouse = Producto("Mouse USB", 12.5)

    # Armo el carrito
    #carrito = Carrito()
    #carrito.add(libro)
    #carrito.add(mouse)

    #orden = Orden(carrito)
    #orden.incluir_envoltorio(True)
    #orden.incluir_envio_express(True)

    #orden.add_listener(EmailListener())
    #orden.add_listener(AnalyticsListener())

    #payment_type = "card"  # puede ser "cash", "card", "mercado-pago"
    #if payment_type.lower() == "card":
        #medio_de_pago = PagoTarjeta("Juan Perez", "4111111111111111")
    #else:
        #medio_de_pago = PagoEfectivo()

    #orden.set_medio_de_pago(medio_de_pago)

    #orden.print_summary()
    #orden.pagar()
