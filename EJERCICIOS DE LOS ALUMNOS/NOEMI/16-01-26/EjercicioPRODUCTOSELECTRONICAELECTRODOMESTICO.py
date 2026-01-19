#Ejercicio 200 con PRODUCTOS, ELECTRONICA Y ELECTRODOMESTICO, Y SUBCLASES.
class Productos:
    def __init__(self,nombre,fabricante,precio):
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Fabricante:",self.fabricante)
        print("Precio:",self.precio,"€")


class Electronica(Productos):

    def __init__(self,nombre,fabricante,precio,modo):
        super().__init__(nombre,fabricante,precio)
        self.modo=modo

    def imprimir(self):
        super().imprimir()
        print("Modo:",self.modo)
            
class Monitores(Electronica):
    def __init__(self,nombre,fabricante,precio,modo,pulgadas="17 pulgadas"):
        super().__init__(nombre,fabricante,precio,modo)
        self.pulgadas=pulgadas

    def imprimir(self):
        super().imprimir()
        print("Pulgadas:",self.pulgadas)
        
class Teclado(Electronica):
    def __init__(self,nombre,fabricante,precio,modo,ergonomia="si"):
        super().__init__(nombre,fabricante,precio,modo)
        self.ergonomia=ergonomia
        
    def imprimir(self):
        super().imprimir()
        print("Seguridad",self.ergonomia)
        
class Portatil(Electronica):
        
     def __init__(self, nombre, fabricante, precio, modo,ram="8 GB"):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram=ram
            
     def imprimir(self):
        super().imprimir()
        print("RAM:",self.ram)
        
class Electrodomesticos(Productos):
    def __init__(self, nombre, fabricante, precio,consumo="A+++"):
        super().__init__(nombre, fabricante, precio)
        self.consumo=consumo
    def imprimir(self):
        super().imprimir()
        print("Consumo:",self.consumo)
class Lavadora(Electrodomesticos):
    def __init__(self, nombre, fabricante, precio, capacidad="9Kg"):
        super().__init__(nombre, fabricante, precio)
        self.capacidad=capacidad
    def imprimir(self):
        super().imprimir()
        print("Capacidad",self.capacidad)
class Frigorifico(Electrodomesticos):
    def __init__(self, nombre, fabricante, precio, tipo="Ecológico" ):
        super().__init__(nombre, fabricante, precio)
        self.tipo=tipo
    def imprimir(self):
        super().imprimir()
        print("Tipo",self.tipo)
class Freidora(Electrodomesticos):
    def __init__(self, nombre, fabricante, precio, temperatura="Máxima"):
        super().__init__(nombre, fabricante, precio)
        self.temperatura=temperatura
    def imprimir(self):
        super().imprimir()
        print("Temperatura:",self.temperatura) 

producto1=Productos("Productos","Marcas","Distintos precios.")
#producto1.imprimir()
print("-"*50)
electronica1=Electronica("Electrónica","variedad de marcas","Precios adaptados a todos los públicos.","Ergonómicos.")
#electronica1.imprimir()
print("-"*50)
monitores1=Monitores("Monitores Samsung","Samsung Display Co., Ltd.", 889, "Ergonómico")
monitores1.imprimir()
print("-"*50)
teclado1=Teclado("Teclado Gaming Wireless","PcComponentes",90,"Ergonómico.")
teclado1.imprimir()
print("-"*50)
portatil1=Portatil("Portatil gaming Victus","HP (Hewlett-Packard)",600, "Ergónomico")
portatil1.imprimir()
print()
print()
electrodomesticos1=Electrodomesticos("Electrodomésticos","Variedad de marcas","Precios adaptados a todos los públicos.", "Eficiencia energética")
#electrodomesticos1.imprimir()
print("-"*50)
lavadora1=Lavadora("Lavadora","Bosch",600,"9Kg")
lavadora1.imprimir()
print("-"*50)
frigorifico1=Frigorifico("Frigorífico Combi","Beko",300,"Ecológico")
frigorifico1.imprimir()
print("-"*50)
freidora1=Freidora("Air Fryer","Xiaomi",50,"De 40ºC hasta 200ºC")
freidora1.imprimir()