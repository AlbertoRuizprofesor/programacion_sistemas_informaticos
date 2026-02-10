"""
 RETO 1: RELACION ENTRE CLASES
 
CreaR un programa en el que vamos a simular una tienda, 
siguiendo el modelo del ejercicio 197:

Clase Producto

Cada producto tiene:

		nombre
		stock inicial 0

Métodos:

	reponer(unidades) → suma stock
	vender(unidades) → resta stock (si hay suficiente)
	retornar_stock() → devuelve el stock
	imprimir() → muestra nombre y stock

Clase Tienda

Tiene 3 productos:

	"Portátil"
	"Ratón"
	"Monitor"

Métodos:

	operar() → repone y vende stock
	stock_total() → calcula stock total de la tienda e imprime los 3 productos
 
 
 la función reponer podría tener esta estructura
 
 
 def reponer(self, unidades):
        self.stock += unidades
        

Pregunta

¿como controlarías el stock?
"""

class Producto:

    def __init__(self, nombre):
        self.nombre = nombre
        self.stock = 0

    def reponer(self, unidades):
        self.stock = self.stock + unidades

    def vender(self, unidades):
        if unidades <= self.stock:
            self.stock = self.stock - unidades
        else:
            print(f"No hay suficiente stock de {self.nombre}")


    def retornar_stock(self):
        return self.stock
    
    def imprimir(self):
            print(self.nombre," quedan ",self.stock, "unidades")


class Tienda:
     
    def __init__(self):
        self.producto1 = Producto("Portatil")
        self.producto2 = Producto("Raton")
        self.producto3 = Producto("Monitor")

    def operar(self):
        self.producto1.reponer(60)
        self.producto1.vender(20)
        self.producto2.reponer(60)
        self.producto2.vender(10)
        self.producto3.reponer(10)
        self.producto3.vender(60)

    def stock_total(self):
        total = self.producto1.retornar_stock() + self.producto2.retornar_stock() + self.producto3.retornar_stock()
        print("El total de stock de productos en tienda es:" , total)
        self.producto1.imprimir()
        self.producto2.imprimir()
        self.producto3.imprimir()

tienda = Tienda()
tienda.operar()
tienda.stock_total()





    

    
 


