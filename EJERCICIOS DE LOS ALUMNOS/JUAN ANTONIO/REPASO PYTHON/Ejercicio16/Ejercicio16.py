# Ejercicio 16. Carrito de compra

class Articulo:
    def __init__(self, titulo, coste):
        self.titulo = titulo
        self.coste = coste


class Cesta:
    def __init__(self):
        self.items = []

    def agregar(self, articulo):
        self.items.append(articulo)

    def quitar(self, titulo):
        self.items = [x for x in self.items if x.titulo != titulo]

    def calcular_total(self):
        return sum(x.coste for x in self.items)

    def __len__(self):
        return len(self.items)

    def mostrar_resumen(self):
        for x in self.items:
            print(f"- {x.titulo}: {x.coste:.2f} €")
        print(f"Total: {self.calcular_total():.2f} €")


# -------------------------
# EJEMPLO
# -------------------------

cesta = Cesta()

a1 = Articulo("Manzanas", 2.50)
a2 = Articulo("Pan", 1.20)
a3 = Articulo("Leche", 1.10)

cesta.agregar(a1)
cesta.agregar(a2)
cesta.agregar(a3)

print("Contenido del carrito:")
cesta.mostrar_resumen()

print(f"Cantidad de artículos: {len(cesta)}")
