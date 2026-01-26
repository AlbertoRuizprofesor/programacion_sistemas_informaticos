"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), 
uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.

Definir dos objetos de la clase Persona.
"""
class Persona:
    # Método para inicializar el atributo 'nombre'
    # Recibe un parámetro 'nom' y lo asigna al atributo de instancia
    def inicializar(self, nom):
        self.nombre = nom

    # Método para imprimir el nombre almacenado en el objeto
    def imprimir(self):
        print("Nombre", self.nombre)

# Bloque principal

# Se crea un objeto de la clase Persona
persona1 = Persona()


# Se asigna un nombre
persona1.inicializar("Pedro")

# Se intenta imprimir el nombre del objeto
persona1.imprimir()

# Se crea un segundo objeto de la clase Persona
persona2 = Persona()

# Se asigna un nombre
persona2.inicializar("Maria")

# Se imprime el nombre del segundo objeto
persona2.imprimir()
