#Ejercicio 200 con alumno y asignatura.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

class Alumno(Persona):
    def __init__(self, nombre,edad, asignatura):
        super().__init__(nombre,edad)
        self.asignatura=asignatura

    def imprimir(self):
        super().imprimir()
        print("Asignatura:",self.asignatura)

persona1=Persona("Noemi",28)
persona1.imprimir()
print("*"*50)
alumno1=Alumno("Noemi", 28, "Matematicas")
alumno1.imprimir()


    