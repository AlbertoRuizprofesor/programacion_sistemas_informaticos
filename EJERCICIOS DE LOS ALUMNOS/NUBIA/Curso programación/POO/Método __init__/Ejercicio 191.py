"""
Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: 
inicializar los valores de x e y que llegan como parámetros, 
imprimir en que cuadrante se encuentra dicho punto
"""

class Puntos:
    def __init__(self):
        self.x = int(input("Ingrese la coordenada x: "))
        self.y = int(input("Ingrese la coordenada y: "))
        
    def imprimir(self):
        if self.x > 0 and self.y > 0:
            print("El punto se encuentra en el primer cuadrante.")
        elif self.x < 0 and self.y > 0:
            print("El punto se encuentra en el segundo cuadrante.")
        elif self.x < 0 and self.y < 0:
            print("El punto se encuentra en el tercer cuadrante.")
        elif self.x > 0 and self.y < 0:
            print("El punto se encuentra en el cuarto cuadrante.")
            
puntos = Puntos()
puntos.imprimir()
