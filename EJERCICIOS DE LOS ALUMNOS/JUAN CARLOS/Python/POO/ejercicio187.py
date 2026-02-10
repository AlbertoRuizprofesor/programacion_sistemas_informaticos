"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota.
Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4).
Definir dos objetos de la clase Alumno.
"""
import funcionesJC as fnJC
#Funciones

class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def esta_regular(self):
        if self.nota <= 4:
            print("Está regular")
        else:
            print("No está regular")


#Main
fnJC.borrarPantalla()
alum1 = Alumno()
alum1.inicializar("Juan Pérez", 7.5)
fnJC.mensaje("Alumno 1")
alum1.imprimir()
alum1.esta_regular()

alum2 = Alumno()
alum2.inicializar("María García", 3.2)
fnJC.mensaje("Alumno 1")
alum2.imprimir()
alum2.esta_regular()

fnJC.mensaje("Alumno 1")
