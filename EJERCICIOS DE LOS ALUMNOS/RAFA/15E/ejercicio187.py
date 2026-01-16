class Alumno:

    def __init__(self,nombre="",nota=""):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal

alumno1=Alumno("pedro",10)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno("laura",8)
alumno2.imprimir()
alumno2.mostrar_estado()
