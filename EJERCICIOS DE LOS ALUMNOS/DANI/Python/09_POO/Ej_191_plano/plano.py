# Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, 
class Punto:
    def __init__(self):
        self.x = int(input("Dame el valor de x: "))
        self.y = int(input("Dame el valor de y: "))
        self.cuadrante()
    # imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print("Cuarto cuadrante")