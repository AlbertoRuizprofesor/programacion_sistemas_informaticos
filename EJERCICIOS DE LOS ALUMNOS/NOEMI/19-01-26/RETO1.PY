#RETO 1: 
class Vehiculos:
    def __init__(self,tipo,marca):
        self.tipo=tipo
        self.marca=marca
    
    def imprimir(self):
        print("Tipo de vehículo:",self.tipo)
        print("Marca del vehículo:",self.marca)
    
class Transporte(Vehiculos):
    def __init__(self, tipo, marca,velocidad):
        super().__init__(tipo, marca)
        self.velocidad=velocidad
    def imprimir(self):
        super().imprimir()
        print("Velocidad permitida de los vehículos de transporte:",self.velocidad)
        
class Construccion(Vehiculos):
    def __init__(self, tipo, marca,pesado):
        super().__init__(tipo, marca)
        self.pesado=pesado
    def imprimir(self):
       super().imprimir()
       print("Cargas pesadas permitidas en vehículos de construcción:",self.pesado)
        
class Autobuces(Transporte):
    def __init__(self, tipo, marca, velocidad,direccion):
        super().__init__(tipo, marca, velocidad)
        self.direccion=direccion
    def imprimir(self):
        super().imprimir()
        print("Los autobuces pueden ser:",self.direccion)
class Motos(Transporte):
    def __init__(self, tipo, marca, velocidad,seguridad="ABS si"):
        super().__init__(tipo, marca, velocidad)
        self.seguridad=seguridad
    def imprimir(self):
        super().imprimir()
        print("Seguridad de la motocicleta:",self.seguridad)
class Coches(Transporte):
    def __init__(self, tipo, marca, velocidad, color):
        super().__init__(tipo,marca,velocidad)
        self.color=color
    def imprimir(self):
        super().imprimir()
        print("Color del vehículo:",self.color)
class Apisonadora(Construccion):
    def __init__(self, tipo, marca, pesado,velocidad):
        super().__init__(tipo, marca, pesado)
        self.velocidad=velocidad
    def imprimir(self):
        super().imprimir()
        print("La velocidad de la apisonadora:",self.velocidad)
class Excavadora(Construccion):
    def __init__(self, tipo, marca, pesado,altura):
        super().__init__(tipo, marca, pesado)
        self.altura=altura
    def imprimir(self):
        super().imprimir()
        print("Altura de la excavadora:",self.altura)
class Hormigonera(Construccion):
    def __init__(self, tipo, marca, pesado,mezcla):
        super().__init__(tipo, marca, pesado)
        self.mezcla=mezcla
    def imprimir(self):
        super().imprimir()
        print("La mezcla a usar en la hormigonera:",self.mezcla)
        
vehiculos1=Vehiculos("Vehículos de transporte o de construcción","Diferentes marcas.")
vehiculos1.imprimir()
print("-"*50)
transporte1=Transporte("Vehículos de transporte","Diferentes marcas","80Kms")
transporte1.imprimir()
print("-"*50)
autobus1=Autobuces("Autobuces","Kimiko autorsbus","80Km","Urbano o Interurbano")
autobus1.imprimir()
print("-"*50)
motos1=Motos("Moto","Toyota","160Kms")
motos1.imprimir()
print("-"*50)
coches1=Coches("Coches","XSARA picasso","180kms","Rojo")
coches1.imprimir()
print("-"*50)
construccion1=Construccion("Construcción","Volvo Construction Equipment (CE)","80kg")
construccion1.imprimir()
print("-"*50)
apisonadora1=Apisonadora("Apisonadora","Kalups segurity","40 revoluciones"," lenta para compactar (1,5 a 2,5 km/h)",)
apisonadora1.imprimir()
print("-"*50)
excavadora1=Excavadora("Excavadora","Yansuengs kome","400kg","7 metros")
excavadora1.imprimir()
print("-"*50)
hormigonera1=Hormigonera("Hormigonera","Mansalanas mecls","60 kg","cemento,agua,arena y grava.")
hormigonera1.imprimir()      