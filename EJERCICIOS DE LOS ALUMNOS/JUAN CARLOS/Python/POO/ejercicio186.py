"""mplementaremos una clase llamada Persona que tendrá como atributo (variable)
	su nombre y dos métodos (funciones),
uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la
	pantalla el contenido del mismo.
Definir dos objetos de la clase Persona.
domicilio, cp, telefono, ciudad, provincia"""
#Biblioteca
import funcionesJC as fnJC
#Clases
class Persona:
	def __init__(self, nombre, domicilio, cp, telefono, ciudad, provincia, apellidos=""): #Con ="" inicializamos el balor a blanco para tener valor por defecto
		self.nombre = nombre
		self.apellidos = apellidos
		self.domicilio = domicilio
		self.cp = cp
		self.telefono =  telefono
		self.ciudad = ciudad
		self.provincia = provincia

	def imprimir(self):
		print(f"=== === === {self.nombre} === === ===")
		print(f"Nombre: {self.nombre}, Apellidos: {self.apellidos}")
		print(f"Domicilio: {self.domicilio}")
		print(f"{self.cp}, {self.ciudad}. {self.provincia}")
		print(f"tlf.: {self.telefono}")
		print(f"=== === === === === ===\n")
#Funciones

#Main
fnJC.borrarPantalla()
#Objeto1
fnJC.mensaje("Objetos")
persona1 = Persona("Carlos", "Calle Mayor 123", 28001, 912345678, "Madrid", "Madrid")
persona1.imprimir()

persona2 = Persona("Ana", "Avenida Blasco Ibáñez 45", 46021, 963147258, "Valencia", "Valencia", "Martínez López")
persona2.imprimir()

persona3 = Persona("Luis", "Plaza de España 7", 41001, 954123456, "Sevilla", "Sevilla", "García Ruiz")
persona3.imprimir()



