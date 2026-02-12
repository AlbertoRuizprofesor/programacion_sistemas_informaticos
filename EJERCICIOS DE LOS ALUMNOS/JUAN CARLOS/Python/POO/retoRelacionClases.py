"""RETO 1: RELACION ENTRE CLASES
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
¿como controlarías el stock?"""
#Importar Biblioteca
import funcionesJC as fnJC
#Clases
class Producto:
    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.stock = 0
    #Métodos
    def reponerUnidades(self, unidades):
        self.stock += unidades
        print(f" ++ Se han añadido {unidades} del producto {self.nombre}.")
        return unidades

    def venderUnidades(self, unidades):
        stockUnidades =  self.retornar_stock()
        if stockUnidades < unidades:
            print("\n#####################################")
            print(f"No se puede completar la operación.\nSolo hay {self.stock} unidades del producto {self.nombre}")
            print("#####################################\n")
        else:
            self.stock -= unidades
            print(f" -- Se han retirado {unidades} del producto {self.nombre}")
            if self.stock == 0:
                print("#####################################")
                print(f"Ya no hay stock del producto {self.nombre}")
                print("#####################################\n")

    def retornar_stock(self):
        return self.stock

    def imprimirProducto(self):
        print(f"Producto: {self.nombre} -- Stock: {self.stock}")

class Tienda:
    #Constructor
    def __init__(self):
        self.producto1 = Producto("Portátil")
        self.producto2 = Producto("Ratón")
        self.producto3 = Producto("Monitor")
    #Métodos
    def operar(self):
        self.producto1.reponerUnidades(5)
        self.producto2.reponerUnidades(10)
        self.producto3.reponerUnidades(15)
        self.producto1.venderUnidades(5)
        self.producto2.venderUnidades(15)

    def stock_total(self):
        stockTotal = self.producto1.retornar_stock() + self.producto2.retornar_stock() + self.producto3.retornar_stock()
        print("-------------- Stock --------------")
        self.producto1.imprimirProducto()
        self.producto2.imprimirProducto()
        self.producto3.imprimirProducto()
        print("-----------------------------------")
        print(f"| Stock Total: {stockTotal}")
#Funciones
def borrarPantalla():
	print("\033c", end="")
#Main
borrarPantalla()
tienda1 = Tienda()
tienda1.operar()
tienda1.stock_total()
