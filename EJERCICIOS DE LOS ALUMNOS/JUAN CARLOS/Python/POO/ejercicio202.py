"""
Ejercicio de clases y herencias
"""
#Clases
class   Productos:
#Constructor
    def __init__(self, nombre, fabricante="", precio=0.0):
        self.nombre = nombre
        self.fabricante = fabricante
        self.precio = precio
#Métodos
    def imprimir(self):
        print(f"Producto: {self.nombre}\nFabricante: {self.fabricante}\nPrecio: {self.precio}€")

class Electronica(Productos):
#Constructor
    def __init__(self, nombre, fabricante, precio, modo=""):
        super().__init__(nombre, fabricante, precio)
        self.modo = modo
# Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Modo: {self.modo}")

class Electrodomestico(Productos):
#Constructor
    def __init__(self, nombre, fabricante, precio, consumo=""):
        super().__init__(nombre, fabricante, precio)
        self.consumo = consumo
#Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Consumo: {self.consumo}")

class Monitores(Electronica):
#Constructor
    def __init__(self, nombre, fabricante, precio, modo, pulgadas):
        super().__init__(nombre, fabricante, precio, modo)
        self.pulgadas = pulgadas
#Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Pulgadas: {self.pulgadas}'")

class Teclado(Electronica):
#Constructor
    def __init__(self, nombre, fabricante, precio, modo, tipo):
        super().__init__(nombre, fabricante, precio, modo)
        self.tipo = tipo
#Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Tipo: {self.tipo}")

class Portatil(Electronica):
#Constructor
    def __init__(self, nombre, fabricante, precio, modo, ram):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram = ram
#Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Ram: {self.ram}GB")

class Lavadora(Electrodomestico):
#Constructor
    def __init__(self, nombre, fabricante, precio, consumo, carga):
        super().__init__(nombre, fabricante, precio, consumo)
        self.carga = carga
#Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Carga: {self.carga} Kg")

class Frigorifico(Electrodomestico):
#Constructor
    def __init__(self, nombre, fabricante, precio, consumo, tipo):
        super().__init__(nombre, fabricante, precio, consumo)
        self.tipo = tipo
#Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Tipo: {self.tipo}")


class Freidora(Electrodomestico):
    # Constructor
    def __init__(self, nombre, fabricante, precio, consumo, temp_max):
        super().__init__(nombre, fabricante, precio, consumo)
        self.temp_max = temp_max

    # Métodos
    def imprimir(self):
        super().imprimir()
        print(f"Temperatura Máxima: {self.temp_max}ºC")

#Funciones
def borrar_pantalla():
    print("\033")

#Main
borrar_pantalla()
print("***************************************************")
producto1 = Productos("Portátil", "Apple", 1999.99)
producto1.imprimir()
print("***************************************************")
electronica1 = Electronica("Ratón", "Corsair", 399.99, "Gamming")
electronica1.imprimir()
print("***************************************************")
electrodomestico1 = Electrodomestico("Nevera", "Balay", 2959.35, "A")
electrodomestico1.imprimir()
print("***************************************************")
monitor1 = Monitores("Monitor", "AOC", 299.35, "Escritorio", 27)
monitor1.imprimir()
print("***************************************************")
teclado1 = Teclado("Teclado", "Razer", 499.35, "Oficina", "ES")
teclado1.imprimir()
print("***************************************************")
portatil1 = Portatil("Portátil", "Apple", 4499.35, "DIOS", 128)
portatil1.imprimir()
print("***************************************************")
lavadora1 = Lavadora("Lavadora", "Fagor", 449.35, "D", 7)
lavadora1.imprimir()
print("***************************************************")
frigorifico1 = Frigorifico("Frigorifico", "Otsein", 399,"A", "Doble")
frigorifico1.imprimir()
print("***************************************************")
freidora1 = Freidora("Freidora", "Frayer", 255.95, "E", 225)
freidora1.imprimir()
print("***************************************************")