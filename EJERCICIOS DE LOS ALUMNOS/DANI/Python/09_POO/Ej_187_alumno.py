# Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    # Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    def calificacion(self):
        if self.nota >= 0 and self.nota <=10:
            if self.nota < 5:
                print("Suspenso\n")
            else:
                print("Aprobado\n")

# Definir dos objetos de la clase Alumno.
alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.calificacion()

alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.calificacion()