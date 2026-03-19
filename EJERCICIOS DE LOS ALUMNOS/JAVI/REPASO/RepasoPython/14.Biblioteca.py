class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"'{self.titulo}' de {self.autor} [{estado}]"

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, titulo, usuario):
        for libro in self.libros:
            if libro.titulo == titulo and not libro.prestado:
                libro.prestado = True
                usuario.libros_prestados.append(libro)
                print(f" Libro '{titulo}' prestado a {usuario.nombre}.")
                return True
        print(f" El libro '{titulo}' no está disponible.")
        return False

    def devolver_libro(self, titulo, usuario):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                libro.prestado = False
                usuario.libros_prestados.remove(libro)
                print(f"re-ingreso: Libro '{titulo}' devuelto por {usuario.nombre}.")
                return True
        return False

    def mostrar_catalogo(self):
        print("\n--- Catálogo de la Biblioteca ---")
        for libro in self.libros:
            print(libro)
        print("---------------------------------\n")

# --- AQUÍ EMPIEZA LA EJECUCIÓN (LO QUE HACÍA FALTA) ---

# 1. Instanciamos la biblioteca
mi_biblioteca = Biblioteca()

# 2. Creamos y agregamos libros
mi_biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabo"))
mi_biblioteca.agregar_libro(Libro("El Principito", "Saint-Exupéry"))
mi_biblioteca.agregar_libro(Libro("1984", "George Orwell"))

# 3. Creamos un usuario
alumno = Usuario("Carlos")

# 4. Probamos las funciones
mi_biblioteca.mostrar_catalogo()

# Pedir un libro
mi_biblioteca.prestar_libro("1984", alumno)

# Intentar pedir el mismo (debería fallar porque ya está prestado)
mi_biblioteca.prestar_libro("1984", alumno)

# Ver cómo quedó el catálogo
mi_biblioteca.mostrar_catalogo()

# Devolver el libro
mi_biblioteca.devolver_libro("1984", alumno)

# Ver catálogo final
mi_biblioteca.mostrar_catalogo()
