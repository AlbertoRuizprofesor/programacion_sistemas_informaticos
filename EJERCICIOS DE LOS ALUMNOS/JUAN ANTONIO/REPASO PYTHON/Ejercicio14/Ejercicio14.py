# Ejercicio 14. Sistema de biblioteca

class Obra:
    def __init__(self, nombre, creador):
        self.nombre = nombre
        self.creador = creador
        self.en_uso = False


class Lector:
    def __init__(self, identificador):
        self.identificador = identificador
        self.prestamos = []


class Coleccion:
    def __init__(self):
        self.catalogo = []

    def añadir_obra(self, obra):
        self.catalogo.append(obra)

    def entregar_obra(self, nombre, lector):
        for obra in self.catalogo:
            if obra.nombre == nombre and not obra.en_uso:
                obra.en_uso = True
                lector.prestamos.append(obra)
                return True
        return False

    def recibir_obra(self, nombre, lector):
        for obra in lector.prestamos:
            if obra.nombre == nombre:
                obra.en_uso = False
                lector.prestamos.remove(obra)
                return True
        return False
    

# -------------------------
# EJEMPLO DE USO
# -------------------------

coleccion = Coleccion()

obra1 = Obra("El Quijote", "Cervantes")
obra2 = Obra("1984", "George Orwell")

coleccion.añadir_obra(obra1)
coleccion.añadir_obra(obra2)

lector1 = Lector("María")

print("Prestando '1984' a María...")
print(coleccion.entregar_obra("1984", lector1))   # True

print("Intentando prestarlo otra vez...")
print(coleccion.entregar_obra("1984", lector1))   # False

print("Devolviendo '1984'...")
print(coleccion.recibir_obra("1984", lector1))    # True
