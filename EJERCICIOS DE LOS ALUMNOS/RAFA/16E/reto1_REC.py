class Producto:
    def __init__(self, nombre,stock_i):
        self.nombre=nombre
        self.stock_i=stock_i
    
    def reponer(self,cantidad):
        self.stock_i=self.stock_i + cantidad
    
    def vender(self,cantidad):
        self.stock_i=self.stock_i - cantidad
    
    def retornar_stock_i(self):
        return self.stock_i
    
    def imprimir(self):
        print(self.nombre,"El inventario es: ",self.stock_i)

class Tienda:
    def __init__(self):
        self.producto1=Producto("Portatil",0)
        self.producto2=Producto("Raton",0)
        self.producto3=Producto("Monitor",0)
    def operar(self):
        self.producto1.reponer(100)
        self.producto1.vender(50)
        self.producto2.reponer(500)
        self.producto2.vender(200)
        self.producto3.reponer(70)
        self.producto3.vender(30)
    
    def inventario(self):
        total=(self.producto1.retornar_stock_i()
        +self.producto2.retornar_stock_i()
        +self.producto3.retornar_stock_i()
        )
        print("El total de dinero del banco es:",total)
        self.producto1.imprimir()
        self.producto2.imprimir()
        self.producto3.imprimir()
        
        

#main
inventario1=Tienda()
inventario1.operar()
inventario1.inventario()