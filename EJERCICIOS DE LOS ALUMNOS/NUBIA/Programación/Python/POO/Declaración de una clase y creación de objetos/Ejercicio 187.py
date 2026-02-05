"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Definir los métodos para inicializar sus atributos, imprimirlos 
y mostrar un mensaje si está regular (nota mayor o igual a 4)
Definir dos objetos de la clase Alumno.
"""

class Alumno:
    
    def __init__(self, nom="", nota=""):
        self.nombre=nom
        self.nota=nota
    

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
        if self.nota >=4:
            print("regular")
        print("------------------------")
           
        
# Bloque principal (objetos)

alumno1 = Alumno("Darío", 10)
alumno1.imprimir()

alumno2 = Alumno("Nubia", 10)
alumno2.imprimir()

alumno3 = Alumno("Dío", 9)
alumno3.imprimir()


