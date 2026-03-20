class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def anadir(self, producto):
        self.productos.append(producto)
        print(f"📦 Añadido: {producto.nombre}")

    def eliminar(self, nombre):
        # Filtra la lista para quitar el producto con ese nombre
        self.productos = [p for p in self.productos if p.nombre != nombre]
        print(f"🗑️ Eliminado: {nombre}")

    def total(self):
        return sum(p.precio for p in self.productos)

    def __len__(self):
        return len(self.productos)

    def resumen(self):
        print("\n--- RESUMEN DE COMPRA ---")
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for p in self.productos:
                print(f"- {p.nombre}: {p.precio:.2f} €")
            print(f"Total: {self.total():.2f} €")
            print(f"Artículos: {len(self)}")
        print("-------------------------\n")

# --- BLOQUE DE EJECUCIÓN ---

# 1. Creamos el carrito
mi_compra = Carrito()

# 2. Creamos algunos productos
p1 = Producto("Teclado Mecánico", 85.50)
p2 = Producto("Ratón Gamer", 45.00)
p3 = Producto("Monitor 4K", 299.99)

# 3. Operamos con el carrito
mi_compra.anadir(p1)
mi_compra.anadir(p2)
mi_compra.anadir(p3)

# 4. Ver el resumen actual
mi_compra.resumen()

# 5. Eliminar un producto (porque sale muy caro el monitor...)
mi_compra.eliminar("Monitor 4K")

# 6. Ver el resumen final
mi_compra.resumen()