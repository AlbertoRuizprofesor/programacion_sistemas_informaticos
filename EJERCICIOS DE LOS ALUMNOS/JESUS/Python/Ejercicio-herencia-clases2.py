#reto herencia de clases 2 vehiculos 


class Vehiculo:
    def __init__(self,nombre,consumo,fabricante,precio):
        self.nombre=nombre
        self.consumo=consumo
        self.fabricante=fabricante
        self.precio=precio

    def imprimir(self,nombre,consumo,fabricante,precio):
        print(self,nombre,consumo,fabricante,precio)

class Transporte(Vehiculo):
    def __init__(self,nombre,consumo,fabricante,precio,modelo,tipo):
        super().__init__(nombre,consumo,fabricante,precio)
        #super().imprimir()
        self.nombre=nombre
        self.consumo=consumo
        self.fabricante=fabricante
        self.precio=precio
        self.modelo=modelo
        self.tipo=tipo
       

# class Construccion(Vehiculo):
#     def __init__(self, nombre, consumo, fabricante, precio,potencia,dimensiones):
#         super().__init__(nombre, consumo, fabricante, precio,potencia,dimensiones)
#         self.nombre=nombre
#         self.consumo=consumo
#         self.fabricante=fabricante
#         self.precio=precio
#         #print(self.nombre,self.fabricante,self.precio,self.consumo,self.modelo,self.tipo)
#         self.potencia=potencia
#         self.dimensiones=dimensiones
#         print(self.nombre,self.fabricante,self.precio,self.consumo,self.potencia,self.dimensiones)

# class Autobuses(Transporte):
#     def __init__(self, nombre, consumo, fabricante, precio, modelo, tipo):
#         super().__init__(nombre, consumo, fabricante, precio, modelo, tipo)
#         self.nombre=nombre
#         self.consumo=consumo
#         self.fabricante=fabricante
#         self.precio=precio
#         print(self.nombre,self.fabricante,self.precio,self.consumo,self.modelo,self.tipo)

# class Motos(Transporte):
#     def __init__(self, nombre, consumo, fabricante, precio, modelo, tipo):
#         super().__init__(nombre, consumo, fabricante, precio, modelo, tipo)
#         self.nombre=nombre
#         self.consumo=consumo
#         self.fabricante=fabricante
#         self.precio=precio
#         print(self.nombre,self.fabricante,self.precio,self.consumo,self.modelo,self.tipo)

class Coches(Transporte):
    def __init__(self, nombre, consumo, fabricante, precio, modelo, tipo):
        super().__init__(nombre, consumo, fabricante, precio, modelo, tipo)
        self.nombre=nombre
        self.consumo=consumo
        self.fabricante=fabricante
        self.precio=precio
        print(self.nombre,self.fabricante,self.precio,self.consumo,self.modelo,self.tipo)

# class Apisonadora(Construccion):
#     def __init__(self, nombre, consumo, fabricante, precio, potencia, dimensiones):
#         super().__init__(nombre, consumo, fabricante, precio, potencia, dimensiones)

# class Excavadora(Construccion):
#     def __init__(self, nombre, consumo, fabricante, precio, potencia, dimensiones):
#         super().__init__(nombre, consumo, fabricante, precio, potencia, dimensiones)

# class Hormigomera(Construccion):
#     def __init__(self, nombre, consumo, fabricante, precio, potencia, dimensiones):
#         super().__init__(nombre, consumo, fabricante, precio, potencia, dimensiones)



coche1=Coches("A3","6/100","Audi","40000","XT","Turismo")
# autobus1=Autobuses("EMT","20/100","Volvo","80000","Ranger","Electrico")
# motos1=Motos("Varanero","4/100","Honda","12000","rxc8","Naked")

# hormigomera1=Hormigomera("aaaaa","bbbbb","ccccc","ddddd","eeeee","fffff")