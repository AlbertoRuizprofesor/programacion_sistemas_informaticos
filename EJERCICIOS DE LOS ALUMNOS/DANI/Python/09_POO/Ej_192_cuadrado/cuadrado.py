#Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos:
class Cuadrado:
    #- inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), 
    def __init__(self):
        self.lado = int(input("Dame el valor de un lado: "))
        self.perimetro()
        self.superficie()
#- imprimir su perímetro y su superficie.
    def perimetro(self):
        self.perim = self.lado * 4
        print(f"Perímetro: {self.perim}")
    
    def superficie(self):
        self.sup = self.lado ** 2
        print(f"Superficie: {self.sup}")
