"""
 RETO 1: RELACION ENTRE CLASES
 
 CreaR un programa en el que vamos a simular una tienda, siguiendo el modelo del ejercicio 197:

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
Respuesta: El stock se controla verificando en el método `vender` que la cantidad a vender sea menor o igual al stock disponible antes de realizar la resta.
"""

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.stock = 0  # stock inicial

    def reponer(self, unidades):
        if unidades > 0:
            self.stock = self.stock + unidades
        else:
            print("Las unidades a reponer deben ser positivas")

    def vender(self, unidades):
        if unidades <= 0:
            print("Las unidades a vender deben ser positivas")
        elif unidades <= self.stock:
            self.stock -= unidades
        else:
            print(f"No hay stock suficiente de {self.nombre}")

    def retornar_stock(self):
        return self.stock

    def imprimir(self):
        print(f"Producto: {self.nombre} | Stock: {self.stock}")


class Tienda:
    def __init__(self):
        self.portatil = Producto("Portátil")
        self.raton = Producto("Ratón")
        self.monitor = Producto("Monitor")

    def operar(self):
        # Reposición de stock
        self.portatil.reponer(10)
        self.raton.reponer(20)
        self.monitor.reponer(5)

        # Venta de productos
        self.portatil.vender(3)
        self.raton.vender(5)
        self.monitor.vender(2)

    def stock_total(self):
        total = (
            self.portatil.retornar_stock()
            + self.raton.retornar_stock()
            + self.monitor.retornar_stock()
        )

        self.portatil.imprimir()
        self.raton.imprimir()
        self.monitor.imprimir()

        print(f"Stock total de la tienda: {total}")


# Programa principal
tienda = Tienda()
tienda.operar()
tienda.stock_total()
