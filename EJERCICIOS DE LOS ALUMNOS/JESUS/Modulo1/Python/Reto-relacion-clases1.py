# RETO 1: RELACION ENTRE CLASES
 
#  CreaR un programa en el que vamos a simular una tienda, siguiendo el modelo del ejercicio 197:

# Clase Producto

# Cada producto tiene:

# 		nombre
# 		stock inicial 0

# Métodos:

# 	reponer(unidades) → suma stock
# 	vender(unidades) → resta stock (si hay suficiente)
# 	retornar_stock() → devuelve el stock
# 	imprimir() → muestra nombre y stock

# Clase Tienda

# Tiene 3 productos:

# 	"Portátil"
# 	"Ratón"
# 	"Monitor"

# Métodos:

# 	operar() → repone y vende stock
# 	stock_total() → calcula stock total de la tienda e imprime los 3 productos
 
 
#  la función reponer podría tener esta estructura
 
 
#  def reponer(self, unidades):
#         self.stock += unidades
        

# Pregunta

# ¿como controlarías el stock?

class Productos:
    def __init__(self,producto):
        self.producto=producto
        self.stock=0

    def compras(self,stock):
        self.stock=self.stock+stock

    def ventas(self,stock):
        self.stock=self.stock-stock


    def stock_real(self):
        return self.stock
    
    def imprim_art(self):
        print("El articulo ", self.producto ," tiene estas unidades disponibles ", self.stock)

class Tienda:
    
    def __init__(self):
        self.producto1=Productos("Portatil")
        self.producto2=Productos("Raton")
        self.producto3=Productos("Teclado")

    def operar(self):
        self.producto1.compras(10)
        self.producto2.compras(50)
        self.producto3.compras(20)
        self.producto1.ventas(3)
        self.producto2.ventas(13)
        self.producto3.ventas(4)
    
    
    def ver_stock(self):
      
        self.producto1.imprim_art()
        self.producto2.imprim_art()
        self.producto3.imprim_art()

#bloque principal 

tienda1=Tienda()
tienda1.operar()
tienda1.ver_stock()
