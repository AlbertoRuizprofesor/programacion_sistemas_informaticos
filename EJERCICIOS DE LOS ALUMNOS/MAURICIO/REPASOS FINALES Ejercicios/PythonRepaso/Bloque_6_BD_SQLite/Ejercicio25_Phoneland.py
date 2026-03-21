import sqlite3


def conectar():
    return sqlite3.connect("phoneland.db")


def crear_tabla():
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            nombre TEXT NOT NULL,
            precio INTEGER
        )
        """
        )


def insertar_producto(producto, nombre, precio):
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (producto, nombre, precio) VALUES (?, ?, ?)",
            (producto, nombre, precio),
        )


def listar_productos():
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()


def buscar_por_nombre(nombre):
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        return cursor.fetchall()


def eliminar_producto(producto_id):
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        return cursor.rowcount


# --- Pruebas de funcionamiento ---

crear_tabla()

# Insertando algunos ejemplos de smartphones
insertar_producto("Smartphone", "iPhone 15", 999)
insertar_producto("Smartphone", "Samsung Galaxy S24", 850)

print("Lista de productos:")
print(listar_productos())

print("\nBuscando por nombre 'iPhone 15':")
print(buscar_por_nombre("iPhone 15"))

print("\nEliminando producto con ID 1...")
eliminar_producto(1)

print("\nLista final:")
print(listar_productos())
