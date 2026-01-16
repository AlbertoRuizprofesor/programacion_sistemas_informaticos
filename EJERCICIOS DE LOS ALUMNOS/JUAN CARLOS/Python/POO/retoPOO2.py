"""RETO 2: POO
Realizar con poo una clase Compras, que además me permite pagar a plazos dicha compra,
con las funciones que sea necesario:
ejemplo:
Producto: Portatil Gaming omnio HP
Precio: 2000 euros
Número de meses a pagar: 10 (En el caso que el número de meses sea mas de 6 meses, un recargo del 5%)
Cuota: (2000+(5%*2000))/10 (numero de meses que voy a estar pagando)
Precio final: (2000+(5%*2000))"""
#Clases
class Compras:
    def __init__(self, nombreProducto, precioProducto, pagoAplazado, meses=0, cuota=0):
        self.nombreProducto = nombreProducto
        self.precioProducto = precioProducto
        self.pagoAplazado = pagoAplazado.lower()
        self.meses = meses
        self.cuota = cuota
        self.pvf = self.calculoPVF()

    def calculoCuota(self, meses):
        cuota = 0
        print(f"cuota: {cuota}")
        cuota = self.precioProducto/meses
        print(f"cuota: {cuota}")
        if meses > 6:
            cuota += (self.precioProducto * 0.05)/self.meses
            print(f"cuota: {cuota}")
        self.cuota = cuota
        return cuota

    def calculoPVF(self):
        pvf = 0
        pvf = self.calculoCuota(self.meses) * self.meses
        return pvf
#Funciones

#Main
compra1 = Compras("Portatil HP", 3000, "s", 7)

print(compra1.__dict__)
