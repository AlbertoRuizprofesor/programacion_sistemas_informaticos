#Ejercicio 200 con persona, alumno,asignatura,empleado,sueldo,profesor,asignatura...
class Persona:
    def __init__(self,tipo,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.tipo=tipo
        
    def imprimir(self):
        print(self.tipo)
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        


class Empleado(Persona):

    def __init__(self, tipo,nombre,edad,sueldo):
        super().__init__(tipo,nombre,edad)
        self.sueldo=sueldo

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")
            
class Alumno(Persona):
    def __init__(self, tipo, nombre,edad, asignatura):
        super().__init__(tipo,nombre,edad)
        self.asignatura=asignatura

    def imprimir(self):
        super().imprimir()
        print("Asignatura:",self.asignatura)
        
class Profesor(Empleado):
    def __init__(self,tipo,nombre,edad,sueldo, asignatura):
        super().__init__(tipo,nombre,edad,sueldo)
        self.asignatura=asignatura

        
    def imprimir(self):
        super().imprimir()
        print("Asignatura:",self.asignatura)


# bloque principal

persona1=Persona("Persona","Jose",20)
#persona1.imprimir()
print("_"*50) 
empleado1=Empleado("Empleada","noemi",28,2000)
#empleado1.imprimir()
empleado1.paga_impuestos()
print("-"*50)
alumno1=Alumno("Alumna","Maria", 13, "Matematicas")
alumno1.imprimir()
print("-"*50)
profesor1=Profesor("Profesor","Mario",39,2600,"Filosofia")
profesor1.imprimir()
profesor1.paga_impuestos()


