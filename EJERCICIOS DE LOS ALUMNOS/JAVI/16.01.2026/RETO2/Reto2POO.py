"""
RETO 2: POO*****************


Realizar con poo una clase Compras, que además me permite pagar a plazos dicha compra, con las funciones que sea necesario:

Ejemplo:

Producto: Portatil Gaming omnio HP
Precio: 2000 euros
Número de meses a pagar: 10 (En el caso que el número de meses sea mas de 6 meses, un recargo del 5%)
Cuota: (2000+(5%*2000))/10 (numero de meses que voy a estar pagando)
Precio final: (2000+(5%*2000))
"""

class Compras:
    def __init__(self, producto, precio, meses):
        self.producto = producto
        self.precio = precio
        self.meses = meses
        self.recargo = 0.05 if meses > 6 else 0

    def calcular_precio_final(self):
        return self.precio + (self.precio * self.recargo)

    def calcular_cuota(self):
        return self.calcular_precio_final() / self.meses

    def mostrar_resumen(self):
        print("\n----- RESUMEN DE LA COMPRA -----")
        print(f"Producto: {self.producto}")
        print(f"Precio inicial: {self.precio} €")
        print(f"Número de meses: {self.meses}")

        if self.recargo > 0:
            print("Recargo aplicado: 5%")
        else:
            print("Recargo aplicado: 0%")

        print(f"Precio final: {self.calcular_precio_final():.2f} €")
        print(f"Cuota mensual: {self.calcular_cuota():.2f} €")


# -------- PROGRAMA PRINCIPAL --------

producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto (€): "))
meses = int(input("Introduce el número de meses a pagar: "))

compra = Compras(producto, precio, meses)
compra.mostrar_resumen()


