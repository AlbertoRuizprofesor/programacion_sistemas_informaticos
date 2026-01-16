"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos:
inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado),
 imprimir su perímetro y su superficie.
"""
#Biblioteca
import funcionesJC as fnJC
#Clase
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        per = 4 * self.lado
        print(f"Perímetro: {per}")

    def superficie(self):
        sup = self.lado ** 2
        print(f"Superficie: {sup}")


#Main
cuad1 = Cuadrado(5)
fnJC.mensaje("Cuadrado lado 5")
cuad1.perimetro()
cuad1.superficie()

cuad2 = Cuadrado(3.5)
fnJC.mensaje("Cuadrado lado 3.5")
cuad2.perimetro()
cuad2.superficie()

fnJC.mensaje("Fin del programa")
