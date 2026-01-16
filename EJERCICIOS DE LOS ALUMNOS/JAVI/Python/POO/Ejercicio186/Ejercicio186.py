"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable)
su nombre y dos métodos (funciones), uno de dichos métodos inicializará el
atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.

Definir dos objetos de la clase Persona.
"""

class Persona:

    def inicializar(self, nombre, apellido="", domicilio="", cp="", telefono="", ciudad="",provincia=""):
        self.nombre=nombre
        self.apellido=apellido
        self.domicilio=domicilio
        self.cp=cp
        self.telefono=telefono
        self.ciudad=ciudad
        self.provincia=provincia

    def imprimir(self):
        print(f"Nombre: {self.nombre}  Apellido: {self.apellido} Domicilio: {self.domicilio} CP: {self.cp} Telefono: {self.telefono} Ciudad: {self.ciudad} Provincia: {self.provincia}")

        


# bloque principal

persona1=Persona()
persona1.inicializar("Pedro", "", "","29010", "","Malaga", "Teba")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla", "Garcia", "Calle Churro", "29030", "66666666", "Cordoba", "Cordoba")
persona2.imprimir()

persona3=Persona()
persona3.inicializar("John", "Pérez")
persona3.imprimir()






