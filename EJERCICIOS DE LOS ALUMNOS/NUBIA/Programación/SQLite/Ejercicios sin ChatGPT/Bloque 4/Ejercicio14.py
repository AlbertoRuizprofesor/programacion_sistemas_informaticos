'''
Modela las clases Libro, Usuario y Biblioteca. La biblioteca debe poder prestar y devolver libros. 

Idea clave: No permitas prestar un libro que ya esté prestado. 
'''

class Libro: 
    def __init__(self, titulo, autor): 
        self.titulo = titulo 
        self.autor = autor 
        self.prestado = False 

class Usuario: 
    def __init__(self, nombre): 
        self.nombre = nombre 
        self.libros_prestados = [] 

class Biblioteca: 
    def __init__(self): 
        self.libros = [] 

    def agregar_libro(self, libro): 
        self.libros.append(libro) 
        print(f"Libro {libro.titulo} agregado a la biblioteca.")
        print("-" * 40)


    def prestar_libro(self, titulo, usuario): 
        for libro in self.libros: 
            if libro.titulo == titulo:
                if not libro.prestado:
                    libro.prestado = True 
                    usuario.libros_prestados.append(libro) 
                    print(f"Libro {titulo} prestado a {usuario.nombre}.")
                    return True 
                else:
                    print(f"ERROR: El libro {titulo} ya esta prestado.")
                    print("-" * 40)

                    return False
        print(f"ERROR: El libro {titulo} no existe en el inventario.")
        print("-" * 40)

        return False 

    def devolver_libro(self, titulo, usuario): 
        for libro in usuario.libros_prestados: 
            if libro.titulo == titulo: 
                libro.prestado = False 
                usuario.libros_prestados.remove(libro) 
                print(f"Libro {titulo} devuelto por {usuario.nombre}.")
                print("-" * 40)

                return True 
        print(f"ERROR: {usuario.nombre} no tiene el libro {titulo}.")
        print("-" * 40)

        return False 


# Main
biblio = Biblioteca()
usuario1 = Usuario("Nubia")
usuario2 = Usuario("Darío")
libro1 = Libro("El Quijote", "Miguel de Cervantes")

biblio.agregar_libro(libro1)
biblio.prestar_libro("El Quijote", usuario1)
biblio.prestar_libro("El Quijote", usuario1)
biblio.devolver_libro("El Quijote", usuario1)
biblio.devolver_libro("El Quijote", usuario1)
biblio.prestar_libro("El Quijote", usuario2)