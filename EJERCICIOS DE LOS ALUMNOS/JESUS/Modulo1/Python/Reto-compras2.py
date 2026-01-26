#
# Reto 3

# Resultado:
# Factura nº: 1
# Producto: Portatil HP GAME
# precio: 2000

# iva: 420
# total: 2420

class Factura:

    def __init__(self,factura,producto,precio):
        self.factura=factura
        self.producto=producto
        self.precio=precio

    def calc_iva(self):
        iva=0.21
        print(f"total iva {self.precio*iva}")
        print(f"total + iva {self.precio+self.precio*iva}")


    def impri_fact(self):
        print(f"Factura {self.factura}, Producto {self.producto}, Precio {self.precio}")




factura1=Factura("nº1","Portatil Gamming HP ",2000)
factura1.impri_fact()
factura1.calc_iva()