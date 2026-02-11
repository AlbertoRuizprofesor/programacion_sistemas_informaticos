"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

Definir dos objetos de la clase Alumno.
"""
class Alumno:

    # Método para inicializar los atributos del alumno.
    # Recibe el nombre y la nota, y los guarda dentro del objeto.
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    # Método que imprime los datos del alumno.
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    # Método que muestra si el alumno está regular o libre.
    # La condición es: si la nota es 4 o más → Regular; si no → Libre.
    def mostrar_estado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")


# Bloque principal del programa

# Se crea el primer objeto Alumno
alumno1 = Alumno()
# Se inicializa con nombre "diego" y nota 2
alumno1.inicializar("diego", 2)
# Se imprimen sus datos
alumno1.imprimir()
# Se muestra su estado (como tiene 2, queda Libre)
alumno1.mostrar_estado()

# Se crea el segundo objeto Alumno
alumno2 = Alumno()
# Se inicializa con nombre "ana" y nota 10
alumno2.inicializar("ana", 10)
# Se imprimen sus datos
alumno2.imprimir()
# Se muestra su estado (como tiene 10, queda Regular)
alumno2.mostrar_estado()
