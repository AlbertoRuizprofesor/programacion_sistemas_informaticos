#RETO 1: RELACION ENTRE CLASES
"""CreaR un programa en el que vamos a simular una tienda, siguiendo el modelo del ejercicio 197:

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
 
class Producto:
     def __init__(self,nombre):
         self.nombre=nombre
         self.stock=0
        
     def reponer_unidades(self,stock):
         self.stock=self.stock+stock
     
     def vender_unidades(self, stock):
        self.stock=self.stock-stock
     
     def retornar_stock(self):
         return self.stock
    
     def imprimir(self):
        print("Hay un stock de",self.stock,"del producto:",self.nombre)
     
class Tienda:
    
    def __init__(self):
        self.producto1=Producto("Portátil")
        self.producto2=Producto("Ratón")
        self.producto3=Producto("Monitor")
        
    def operar(self):
        self.producto1.reponer_unidades(2)
        self.producto2.reponer_unidades(3)
        self.producto3.reponer_unidades(4)
        
        self.producto1.vender_unidades(1)
        self.producto2.vender_unidades(3)
        self.producto3.vender_unidades(2)
        
        print("Operaciones realizadas (reponer y vendido).")
    
    def stock_total(self):
        print("Inventario y total:")
        self.producto1.imprimir()
        self.producto2.imprimir()
        self.producto3.imprimir()
        
        total=(self.producto1.retornar_stock()+
               self.producto2.retornar_stock()+
               self.producto3.retornar_stock())
        print("Total de stock es:",total)
        
                
tienda1=Tienda()
tienda1.operar()
tienda1.stock_total()
    
        
        
         
         
        
        
        
         