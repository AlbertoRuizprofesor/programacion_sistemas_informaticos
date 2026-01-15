class Persona:

    def inicializar(self,nombre, ciudad, apellidos="", CP=""):
        self.nombre=nombre
        self.apellidos=apellidos
        self.CP=CP
        self.ciudad=ciudad

    def imprimir(self):
        print(f"Nombre: {self.nombre} Apellidos: {self.apellidos} CP: {self.CP} Ciudad: {self.ciudad}")


# bloque principal

persona1=Persona()
persona1.inicializar("Pedro", ciudad="Malaga")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla", "Blum", "29140", "Malaga")
persona2.imprimir()

persona3=Persona()
persona3.inicializar("laly", apellidos="Jimenez", ciudad="Malaga")
persona3.imprimir()

