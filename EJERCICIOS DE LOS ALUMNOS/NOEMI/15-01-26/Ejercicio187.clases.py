#Ejercicio 187: Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
#Definir dos objetos de la clase Alumno.

class Alumno:
    def __init__(self,nombre="",nota=""):
        self.nombre=nombre
        self.nota=nota
        
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
        
    def mostar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("libre")
            
    def separaciobn(self):
        print("*************************")
            
            
alumno1=Alumno("Noemi",10)
alumno1.imprimir()
alumno1.mostar_estado()
alumno1.separaciobn()

#********************************

alumno2=Alumno("Maria",3)
alumno2.imprimir()
alumno2.mostar_estado()