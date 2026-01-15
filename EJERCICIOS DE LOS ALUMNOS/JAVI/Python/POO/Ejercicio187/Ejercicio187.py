"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota.
Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
Definir dos objetos de la clase Alumno.
"""

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mostrar_estado(self):
        if self.nota > 4:
            print("Regular")
        else:
            print("Mal")


alumno1 = Alumno("Paco" , 7)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2 = Alumno("Lucía", 3)
alumno2.imprimir()
alumno2.mostrar_estado()









