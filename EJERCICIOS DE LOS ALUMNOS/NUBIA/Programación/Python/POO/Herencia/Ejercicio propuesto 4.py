# Clase principal
class Vehículos:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def imprimir(self):
        print(f"Tipo de vehículo: {self.tipo}")
  
      
# Vehículos de transporte
class Transporte(Vehículos):
    def __init__(self, tipo, categoriat, color, cilindrada=0):
        super().__init__(tipo)
        self.categoriat = categoriat
        self.color = color
        self.cilindrada = cilindrada
        
    def imprimir(self):
        super().imprimir()
        print(f"Vechículo de transporte: {self.categoriat}")
        print(f"Color del vehículo: {self.color}")
        if self.cilindrada:
            print(f"Cilindrada: {self.cilindrada}")
        
class Autobús(Transporte):
    def __init__(self, tipo, categoriat, color, direccion):
        super().__init__(tipo, categoriat, color, cilindrada=0)
        self.direccion = direccion
    
    def imprimir(self):
        super().imprimir()
        print(f"Dirección: {self.direccion}")

# Vehículos de construcción      
class Construcción(Vehículos):
    def __init__(self, tipo, categoriac, marca):
        super().__init__(tipo)
        self.categoriac = categoriac
        self.marca = marca
        
    def imprimir(self):
        super().imprimir()
        print(f"Vehículo de construcción: {self.categoriac}")
        print(f"Marca del vehículo: {self.marca}")


# Bloque principal
coche1 = Transporte("transporte", "coche", "negro")
coche1.imprimir()
print("-"*50)
moto1 = Transporte("transporte", "moto", "verde", "125cc")
moto1.imprimir()
print("-"*50)
autobus1 = Autobús("Transporte", "autobús", "blanco", "urbano")
autobus1.imprimir()
print("-"*50)
construccion1 = Construcción("construcción", "apisonadora", "CAT")
construccion1.imprimir()
print("-"*50)
construccion2 = Construcción("construcción", "excavadora", "Sany")
construccion2.imprimir()
print("-"*50)
construccion3 = Construcción("construcción", "hormigonera", "Hitachi")
construccion3.imprimir()
