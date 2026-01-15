#Ejercicio 192: Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.

class Cuadrado:
    
    def __init__(self,lado):
        self.lado=lado
        
    def imprimir_perimetro(self):
        per=self.lado*4
        print("El perimetro del cuadrado es: ",per)
        
    def imprimir_superficie(self):
        sup=self.lado*self.lado
        print("La superficie del cuadrado es: ",sup)
        
cuadrado1=Cuadrado(12)
cuadrado1.imprimir_perimetro()
cuadrado1.imprimir_superficie()    