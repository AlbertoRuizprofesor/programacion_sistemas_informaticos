"""
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. 
Mostrar un menú de opciones que permita:

1- Cargar alumnos.

2- Listar alumnos.

3- Mostrar alumnos con notas mayores o iguales a 7.

4- Finalizar programa.
"""

class Alumnos:

    def __init__(self):
        self.alumnos = []
        self.notas = []

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))

            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.notas7()

    def cargar(self):
        for x in range(5):
            nombre = input("Nombre del alumno: ")
            self.alumnos.append(nombre)
            nota = float(input("Nota: "))
            self.notas.append(nota)

    def listar(self):
        print("Lista de alumnos: ")
        for x in range(len(self.alumnos)):
            print(self.alumnos[x], self.notas[x])
        print("**************************")

    def notas7(self):
        print("Alumnos con notas mayores a 7: ")
        for x in range (5):
            if self.notas[x] >= 7:
                print(self.alumnos[x] , self.notas[x])
        print("************************")

alumnos=Alumnos()
alumnos.menu()    




