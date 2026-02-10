#RETO 2: POO***************************************************************************************************************
#Realizar con poo una clase Compras, que además me permite pagar a plazos dicha compra, con las funciones que sea necesario:

#ejemplo:

#Producto: Portatil Gaming omnio HP
#Precio: 2000 euros
#Número de meses a pagar: 10 (En el caso que el número de meses sea mas de 6 meses, un recargo del 5%)
#Cuota: (2000+(5%*2000))/10 (numero de meses que voy a estar pagando)
#Precio final: (2000+(5%*2000))
class Compras:
    def __init__(self, producto, precio, meses):
        self.producto = producto
        self.precio = precio
        self.meses = meses

    def calcular_recargo(self):
        if self.meses > 6:
            return self.precio * 0.05
        else:
            return 0

    def precio_final(self):
        return self.precio + self.calcular_recargo()

    def cuota_mensual(self):
        return self.precio_final() / self.meses

    def mostrar_compra(self):
        print(f"Producto: {self.producto}")
        print(f"Precio inicial: {self.precio:.2f} euros")
        print(f"Número de meses: {self.meses}")
        print(f"Recargo: {self.calcular_recargo():.2f} euros")
        print(f"Precio final: {self.precio_final():.2f} euros")
        print(f"Cuota mensual: {self.cuota_mensual():.2f} euros")

compra = Compras("Portátil Gaming Omnio HP", 2000, 10)
compra.mostrar_compra()

