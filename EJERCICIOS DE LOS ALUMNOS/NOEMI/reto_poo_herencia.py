class Productos:
    
    def __init__(self, nombre, fabricante, precio):
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("fabricante:", self.fabricante)
        print("precio: ", self.precio )
        
    
class Electronica(Productos):
    
    def __init__(self, nombre, fabricante, precio, modo="gaming"):
        super().__init__(nombre, fabricante, precio) 
        self.modo=modo
        
    def imprimir(self):
        super().imprimir()
        print("modo: ", self.modo)
        
class Monitores(Electronica):
    
    def __init__(self, nombre, fabricante, precio, modo="gaming", pulgadas="17"):
        super().__init__(nombre, fabricante, precio, modo)
        self.pulgadas=pulgadas
    
    def imprimir(self):
        super().imprimir()
        print("pulgadas: ", self.pulgadas)

class Teclados(Electronica):
    
    def __init__(self, nombre, fabricante, precio, modo="gaming", ergonomico="si"):
        super().__init__(nombre, fabricante, precio, modo)
        self.ergonomico=ergonomico
    
    def imprimir(self):
        super().imprimir()
        print("ergonomico: ", self.ergonomico)

class Portatil(Electronica):
    
    def __init__(self, nombre, fabricante, precio, modo="gaming", ram=8):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram=ram
    def imprimir(self):
        super().imprimir()
        print("ram: ", self.ram)

class Electrodomesticos(Productos):
    
    def __init__(self, nombre, fabricante, precio, tipo="Lux"):
        super().__init__(nombre, fabricante, precio)
        self.tipo=tipo
    
    def imprimir(self):
        super().imprimir()
        print("tipo: ", self.tipo)
        
class Lavadora(Electrodomesticos):
    
    def __init__(self, nombre, fabricante, precio, tipo="lux", carga=7):
        super().__init__(nombre, fabricante, precio, tipo)
        self.carga=carga
    def imprimir(self):
        super().imprimir()
        print("carga: ", self.carga)
        
class Neveras(Electrodomesticos):
    
    def __init__(self, nombre, fabricante, precio, tipo="lux", hielo=""):
        super().__init__(nombre, fabricante, precio, tipo)
        self.hielo=hielo
    def imprimir(self):
        super().imprimir()
        print("hielo: ", self.hielo)

class Freidoras(Electrodomesticos):
    
    def __init__(self, nombre, fabricante, precio, tipo="lux", temp=""):
        super().__init__(nombre, fabricante, precio, tipo)
        self.temp=temp
    def imprimir(self):
        super().imprimir()
        print("temp: ", self.temp)
        


    
#bloque principal


    
productos1=Productos("monitores", "Xiaomi", 210)
#productos1.imprimir()
electronica1=Electronica("monitores", "Xiaomi", 120, "standard")
#electronica1.imprimir()
monitores1=Monitores("monitores", "Xiaomi", 120, "standard", "17")
monitores1.imprimir()
print()
teclados1=Teclados("teclados", "Microsoft", 50, "standard", "si")
teclados1.imprimir()
print()
portatil1=Portatil("Portatil", "Omen", 1300, "standard", "8")
portatil1.imprimir()
print()
electrodomesticos1=Electrodomesticos("Nevera", "Saba", 500, "lux")
#electrodomesticos1.imprimir()
lavadoras1=Lavadora("lavadora", "Saba", 500, "lux", 7)
lavadoras1.imprimir()
print()
neveras1=Neveras("nevera", "Saba", 400, "lux", "No Frost")
neveras1.imprimir()
print()
freidora1=Freidoras("AirFrier", "Saba", 200, "lux", "370º")
freidora1.imprimir()

