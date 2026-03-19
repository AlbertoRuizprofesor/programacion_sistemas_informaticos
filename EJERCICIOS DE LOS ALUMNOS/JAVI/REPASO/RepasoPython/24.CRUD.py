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
        cursor.execute("INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)", (titulo, autor, anio))

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

# --- EJECUCIÓN CON SALIDA LIMPIA ---

# 1. Preparamos la base
crear_tabla()

# 2. Insertamos datos de prueba
insertar_libro("1984", "George Orwell", 1949)
insertar_libro("El Quijote", "Miguel de Cervantes", 1605)
print(" Libros insertados.\n")

# 3. Listamos de forma bonita
print("--- Catálogo Completo ---")
for libro in listar_libros():
    print(f"ID: {libro[0]} | Título: {libro[1]:<15} | Autor: {libro[2]}")

# 4. Probamos la búsqueda
print(f"\n--- Búsqueda de Orwell ---")
busqueda = buscar_por_autor("George Orwell")
for b in busqueda:
    print(f"Encontrado: {b[1]} ({b[3]})")

# 5. Probamos eliminar (borramos el primer libro que encuentre con ID 1)
borrados = eliminar_libro(1)
print(f"\n Se han borrado {borrados} libro(s) con ID 1.")