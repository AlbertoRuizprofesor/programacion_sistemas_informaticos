class Vehiculos:
    
    def __init__(self, nombre, fabricante, precio):
        self.nombre=nombre
        self.fabricante=fabricante
        self.precio=precio
        
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("fabricante:", self.fabricante)
        print("precio: ", self.precio )
        
    
class Transporte(Vehiculos):
    
    def __init__(self, nombre, fabricante, precio, modo="Extras"):
        super().__init__(nombre, fabricante, precio) 
        self.modo=modo
        
    def imprimir(self):
        super().imprimir()
        print("modo: ", self.modo)
        
class Buses(Transporte):
    
    def __init__(self, nombre, fabricante, precio, modo="Extras", plazas="20"):
        super().__init__(nombre, fabricante, precio, modo)
        self.plazas=plazas
    
    def imprimir(self):
        super().imprimir()
        print("plazas: ", self.plazas)

class Motos(Transporte):
    
    def __init__(self, nombre, fabricante, precio, modo="Sin Extras", color="tricolor"):
        super().__init__(nombre, fabricante, precio, modo)
        self.color=color
    
    def imprimir(self):
        super().imprimir()
        print("color: ", self.color)

class Coches(Transporte):
    
    def __init__(self, nombre, fabricante, precio, modo="Extras", puertas=5):
        super().__init__(nombre, fabricante, precio, modo)
        self.puertas=puertas
    def imprimir(self):
        super().imprimir()
        print("puertas: ", self.puertas)

class Construccion(Vehiculos):
    
    def __init__(self, nombre, fabricante, precio, peso_kg="4500"):
        super().__init__(nombre, fabricante, precio)
        self.peso_kg=peso_kg
    
    def imprimir(self):
        super().imprimir()
        print("peso_kg: ", self.peso_kg)
        
class Apisonadora(Construccion):
    
    def __init__(self, nombre, fabricante, precio, peso_kg="3500", conductor="si"):
        super().__init__(nombre, fabricante, precio, peso_kg)
        self.conductor=conductor
    def imprimir(self):
        super().imprimir()
        print("conductor: ", self.conductor)
        
class Excavadora(Construccion):
    
    def __init__(self, nombre, fabricante, precio, peso_kg="3500", tipo_pala="Excavar"):
        super().__init__(nombre, fabricante, precio, peso_kg)
        self.tipo_pala=tipo_pala
    def imprimir(self):
        super().imprimir()
        print("tipo_pala: ", self.tipo_pala)

class Hormigonera(Construccion):
    
    def __init__(self, nombre, fabricante, precio, peso_kg="3500", capacidad_bombo="2T"):
        super().__init__(nombre, fabricante, precio, peso_kg)
        self.capacidad_bombo=capacidad_bombo
    def imprimir(self):
        super().imprimir()
        print("capacidad del bombo: ", self.capacidad_bombo)
        


    
#bloque principal


    
vehiculos1=Vehiculos("transporte", "Ebro", 50000)
#vehiculos1.imprimir()
transporte1=Transporte("buses", "Ebro", 50000, "Extras")
#electronica1.imprimir()
buses1=Buses("Minibus:", "Ebro", 50000, "Extras", "20")
buses1.imprimir()
print()
motos1=Motos("Scoopy", "Honda", 7000, "standard", "roja/blanca")
motos1.imprimir()
print()
coches1=Coches("leon", "Seat", 20000, "C/Extras", "5")
coches1.imprimir()
print()
construccion1=Construccion("apisonadora", "Golen", 100000, "20000")
#construccion1.imprimir()
apisonadoras1=Apisonadora("apisonadora", "golen", 150000, "20000", "No")
apisonadoras1.imprimir()
print()
excavadora1=Excavadora("Miniexcavadora", "Saba", 100000, "15000", "recoger")
excavadora1.imprimir()
print()
hormigonera1=Hormigonera("Hormigonera", "Cabeza", 75000, "10000", "3T")
hormigonera1.imprimir()

