#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

#Definir dos objetos de la clase Alumno.

class Alumno:


    def __init__(self,nombre,nota):  # __init__ doble guion 
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} Nota: {self.nota}")

    def mostrar_estado(self):
        if self.nota<=4:
            print("Suspenso")
        else:
            print("Aprobado")


#bloque principal

alumno1=Alumno("Diego",2)
#alumno1.inicializar("Diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno("Ana",10)
#alumno2.inicializar("Ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()

alumno3=Alumno("Paco",5)
#alumno3.inicializar("Paco",5)
alumno3.imprimir()
alumno3.mostrar_estado()

alumno4=Alumno("Luis",4)
#alumno4.inicializar("Luis",4)
alumno4.imprimir()
alumno4.mostrar_estado()