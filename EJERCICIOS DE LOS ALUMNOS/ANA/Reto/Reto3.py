#Reto 3

#Resultado:
#Factura nº: 1
#Producto: Portatil HP GAME
#precio: 2000

#iva: 420
#total: 2420
class Factura:
    def __init__(self, numero, producto, precio):
        self.numero = numero
        self.producto = producto
        self.precio = precio

    def calcular_iva(self):
        return self.precio * 0.21

    def calcular_total(self):
        return self.precio + self.calcular_iva()

    def mostrar_factura(self):
        print(f"Factura nº: {self.numero}")
        print(f"Producto: {self.producto}")
        print(f"Precio: {self.precio:.2f} €")
        print(f"IVA: {self.calcular_iva():.2f} €")
        print(f"Total: {self.calcular_total():.2f} €")

factura = Factura(1, "Portátil HP GAME", 2000)
factura.mostrar_factura()
