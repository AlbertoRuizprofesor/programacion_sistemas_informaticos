class Alumno:
    
    # El método __init__ es el constructor estándar en Python
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def mostrar_estado(self):
        if self.nota >= 4:
            print("Estado: Regular")
        else:
            print("Estado: Libre")


# bloque principal

# Ahora pasamos los datos directamente entre los paréntesis al crear el objeto
alumno1 = Alumno("Julieta", 8)
alumno1.imprimir()
alumno1.mostrar_estado()

print("-" * 20) # Separador visual

alumno2 = Alumno("Marcos", 3)
alumno2.imprimir()
alumno2.mostrar_estado()