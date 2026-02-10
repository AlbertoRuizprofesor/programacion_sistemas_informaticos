"""
Clase Club con 3 Socios internos. Imprime socio con mayor antigüedad.
"""

#Clases


class Socio:
    def __init__(self):
        self.nombre = input("Nombre socio: ")
        self.antiguedad = int(input("Antigüedad (años): "))

    def imprimir(self):
        print(f"Socio: {self.nombre}, Antigüedad: {self.antiguedad} años")


class Club:
    def __init__(self):
        # 3 socios creados en Club
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def socio_mayor_antiguedad(self):
        socios = [self.socio1, self.socio2, self.socio3]
        socio_max = max(socios, key=lambda s: s.antiguedad)
        return socio_max.nombre

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")
def borrarPantalla():
	print("\033c", end="")
#Main
borrarPantalla()
club = Club()
mensaje("Socios cargados")

mensaje("Socio con mayor antigüedad")
print(f"{club.socio_mayor_antiguedad()}")

mensaje("Fin del programa")
