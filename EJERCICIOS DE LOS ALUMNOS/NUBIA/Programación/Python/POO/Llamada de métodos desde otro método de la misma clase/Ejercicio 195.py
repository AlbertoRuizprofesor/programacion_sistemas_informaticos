"""
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:

1- Cargar alumnos.

2- Listar alumnos.

3- Mostrar alumnos con notas mayores o iguales a 7.

4- Finalizar programa.
"""

class Alumnos:
    def __init__(self):
        self.nombres = []
        self.notas = []
    
    def menu(self):
        print("1- Cargar alumnos.")
        print("2- Listar alumnos.")
        print("3- Mostrar alumnos con notas mayores o iguales a 7.")
        print("4- Finalizar programa.")
        print("--------------------------------")
        eleccion = int(input("Ingrese una opcción: "))
        if eleccion != 4:
            if eleccion == 1:
                self.cargar()
                print("--------------------------------")
                self.menu() # self.(menu) para volver al menú con los datos ya guardados.
            elif eleccion == 2:
                self.listar()
                print("--------------------------------")
                self.menu()
            elif eleccion == 3:
                self.notasmayores()
                print("--------------------------------")
                self.menu()
        else:
            self.finalizar()        
            
    def cargar(self):
        for x in range(5):
            nombre = input(f"Ingrese el nombre del alumno {x+1}: ")
            self.nombres.append(nombre)
            nota = int(input("Ingrese la nota del alumno: "))
            self.notas.append(nota)
            
    def listar(self):
        for x in range(5):
            print(f"Alumno: {self.nombres[x]} - Nota: {self.notas[x]}")
            print("--------------------------------")
    
    def notasmayores(self):
        for x in range(5):
            if self.notas[x] >= 7:
                print(f"Alumno: {self.nombres[x]} - Nota: {self.notas[x]}")
    
    def finalizar(self):
        print("Programa finalizado")
        

# Bloque principal

alumno1 = Alumnos()
alumno1.menu()
