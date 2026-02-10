"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: 
inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), 
imprimir su perímetro y su superficie.
"""

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        self.area = self.lado * self.lado
        return self.area
    
    def imprimir(self):
        print(f"El perímetro es: {self.perimetro()}")
        print(f"El área es: {self.area()}")
        
# Bloque principal

cuadrado1 = Cuadrado(3) # Meto el valor, porque no ha sido un input
cuadrado1.imprimir()