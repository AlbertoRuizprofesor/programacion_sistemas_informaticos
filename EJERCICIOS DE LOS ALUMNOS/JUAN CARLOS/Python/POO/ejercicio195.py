"""
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas.
Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.
"""
#Import Biblioteca
import funcionesJC as fnJC
#Funciones

#Clases
class AlumnoNota:
    def __init__(self):
        self.nombres = []
        self.notas = []

    def menuPrincipal(self):
        seleccion = 0
        while seleccion != 4:
            seleccion = fnJC.menuInicio(f"Listado Alumnos")
            if seleccion == 1:
               self.cargarAlumno()
            if seleccion == 2:
                self.listarAlumnos()
            if seleccion == 3:
                self.listarNota_7()

    def cargarAlumno(self):
        nombre = input("Introduce el nombre: ")
        self.nombres.append(nombre)
        nota = float(input(f"Introduce la nota de {nombre}: "))
        self.notas.append(nota)

    def listarAlumnos(self):
        cntAlumnos = len(self.nombres)
        for cnt in range(cntAlumnos):
              print(f"Alumno: {self.nombres[cnt]}, nota: {self.notas[cnt]}")
    def listarNota_7(self):
        for cnt in range(len(self.notas)):
            if self.notas[cnt] >= 7:
                print(f"Alumno: {self.nombres[cnt]}, nota: {self.notas[cnt]}")
#Main
fnJC.borrarPantalla()
#fnJC.mensaje("Carga de valores")
historia = AlumnoNota()
historia.menuPrincipal()




