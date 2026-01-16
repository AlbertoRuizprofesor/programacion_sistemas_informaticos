class Producto:

    def __init__(self, nombre):
        self.nombre = nombre
        self.stock = 0

    def reponer(self, stock):
        self.stock = self.stock + stock

    def vender(self, stock):
        if stock > 0:
            self.stock = self.stock - stock
        else:
            print("No hay Stock")

    def retornar_stock(self):
        return self.stock

    def imprimir(self):
        print(f"De {self.nombre} hay {self.stock} en la tienda")


class Tienda:

    def __init__(self):
        self.producto1 = Producto("Monitor")
        self.producto2 = Producto("Teclado")
        self.producto3 = Producto("Ratones")

    def operar(self):
        self.producto1.reponer(100)
        self.producto2.reponer(150)
        self.producto3.reponer(200)
        self.producto3.vender(150)

    def depositos_totales(self):
        total = (
            self.producto1.retornar_stock()
            + self.producto2.retornar_stock()
            + self.producto3.retornar_stock()
        )
        print("El total de productos de la tienda es:", total)
        self.producto1.imprimir()
        self.producto2.imprimir()
        self.producto3.imprimir()


# bloque principal

tienda1 = Tienda()
tienda1.operar()
tienda1.depositos_totales()
