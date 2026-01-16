#RETO 2: Realizar con poo una clase Compras, que además me permite pagar a plazos dicha compra, con las funciones que sea necesario:
"""ejemplo:

Producto: Portatil Gaming omnio HP
Precio: 2000 euros
Número de meses a pagar: 10 (En el caso que el número de meses sea mas de 6 meses, un recargo del 5%)
Cuota: (2000+(5%*2000))/10 (numero de meses que voy a estar pagando)
Precio final: (2000+(5%*2000))"""

class Compra:
    def __init__(self, nombre="",precio=""):
        self.nombre=nombre
        self.precio=precio
        
    def calculo(self):
        meses=10
        recargo=0
        
        if meses>6:
            recargo=self.precio*0.05
            
        preciofinal=self.precio+recargo
        cuota=preciofinal/meses
        
        print(f"Producto: {self.nombre}, precio: {self.precio}")
        print("Número de meses a pagar:",meses," don recargo del 5 por ciento al ser mas de 6 meses:",recargo,"y con cuota mensual de :",cuota)
        print("Precio final:",preciofinal)
        
compra1=Compra("Portatil gaming omnio HP", 2000)
compra1.calculo()
            
        
        
            