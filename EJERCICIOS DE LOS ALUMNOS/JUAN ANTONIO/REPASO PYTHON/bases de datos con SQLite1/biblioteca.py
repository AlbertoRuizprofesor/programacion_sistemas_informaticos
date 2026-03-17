import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")

def crear_tabla():
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            anio INTEGER
        )
        """)

def insertar_libro(titulo, autor, anio):
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)",
            (titulo, autor, anio)
        )

def listar_libros():
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libros")
        return cursor.fetchall()

def buscar_por_autor(autor):
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libros WHERE autor = ?", (autor,))
        return cursor.fetchall()

def eliminar_libro(libro_id):
    with conectar() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?", (libro_id,))
        return cursor.rowcount


# --- PRUEBAS DEL PROGRAMA ---
crear_tabla()

insertar_libro("1984", "George Orwell", 1949)
insertar_libro("El Quijote", "Miguel de Cervantes", 1605)

print("📘 Lista de libros:")
print(listar_libros())

print("\n🔎 Libros de George Orwell:")
print(buscar_por_autor("George Orwell"))

print("\n🗑️ Eliminando libro con id 1...")
print("Filas eliminadas:", eliminar_libro(1))

print("\n📘 Lista actualizada:")
print(listar_libros())
