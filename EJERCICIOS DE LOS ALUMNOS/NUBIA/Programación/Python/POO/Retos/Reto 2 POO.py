"""
Realizar con poo una clase Compras, que además me permite pagar a plazos dicha compra, con las funciones que sea necesario:

ejemplo:
Producto: Portatil Gaming omnio HP
Precio: 2000 euros
Número de meses a pagar: 10 (En el caso que el número de meses sea mas de 6 meses, un recargo del 5%)
Cuota: (2000+(5%*2000))/10 (numero de meses que voy a estar pagando)
Precio final: (2000+(5%*2000))
"""

class Compras:
    def __init__(self):
        print("CATÁLOGO DE PRODUCTOS:")
        print("Portátil")
        print("Móvil")
        print("Tablet")
        self.producto = (input("Ingrese el producto: "))
        self.meses = int(input("Ingrese en cuántos meses quiere pagar: "))
        print("-"*50)
        
    def precios(self):
        if self.producto == "PORTÁTIL" or "PORTATIL" or "Portátil" or "Portatil" or "portátil" or "portatil":
            self.precio = 2000
        elif self.producto == "MÓVIL" or "MOVIL" or "Móvil" or "Movil" or "móvil" or "movil":
            self.precio = 500
        elif self.producto == "TABLET" or "Tablet" or "tablet":
            self.precio = 250

    def pagar(self):
        if self.meses > 6:
            intereses = self.precio * 0.05
            cuota = (self.precio + intereses) / self.meses
            precio_final = self.precio + intereses
            print(f"Producto: {self.producto}")
            print(f"Precio: {self.precio} euros")
            print(f"Numero de meses a pagar: {self.meses}")
            print(f"Cuota: {cuota:.2f} euros")
            print(f"Precio final: {precio_final:.2f} euros")
        else:
            cuota = self.precio / self.meses
            print(f"Producto: {self.producto}")
            print(f"Precio: {self.precio} euros")
            print(f"Numero de meses a pagar: {self.meses}")
            print(f"Cuota: {cuota:.2f} euros")
            print(f"Precio final: {self.precio:.2f} euros")
    
# Bloque principal
compra = Compras()
compra.precios()
compra.pagar()