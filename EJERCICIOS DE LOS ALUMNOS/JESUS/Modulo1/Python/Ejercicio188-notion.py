#Confeccionar una clase que permita carga el nombre y la edad de una persona. 
# Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

class Persona:

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print(f"Nombre: {self.nombre}, edad {self.edad}")

    def mayor_edad(self):
        if self.edad>=18:
            print("Es mayor de edad")
        else:
            print("No es mayor ")


# Bloque principal 


persona1=Persona("Antonio",18)
persona1.imprimir()
persona1.mayor_edad()


persona2=Persona("Luis",28)
persona2.imprimir()
persona2.mayor_edad()


persona3=Persona("Pepe",17)
persona3.imprimir()
persona3.mayor_edad()

persona4=Persona("Paco",67)
persona4.imprimir()
persona4.mayor_edad()
