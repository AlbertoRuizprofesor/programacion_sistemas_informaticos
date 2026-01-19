#Ejercicio 188: Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)


class Persona:
    def __init__(self,nom="",edad=""):
        self.nom=nom
        self.edad=edad
        
    def imprimir(self):
        print("Nombre:",self.nom)
        print("Edad", self.edad)
        
    def mayor_edad(self):
        if self.edad>=18:
            print("Es mayor de edad.")
        else:
            print("Es menor de edad.")
            
    def separacion(self):
        print("****************************")
        
persona1=Persona("Noemi",28)
persona1.imprimir()
persona1.mayor_edad()
persona1.separacion()

        