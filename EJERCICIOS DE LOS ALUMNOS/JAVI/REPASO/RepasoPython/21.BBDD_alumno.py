import sqlite3

# 1. Conectamos (si no existe, se crea el archivo academia.db)
conexion = sqlite3.connect("academia.db")
cursor = conexion.cursor()

# 2. Creamos la tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    nota REAL
)
""")

# 3. Insertamos datos (Solo si la tabla está vacía para no duplicar)
cursor.execute("SELECT COUNT(*) FROM alumnos")
if cursor.fetchone()[0] == 0:
    alumnos = [
        ("Ana", 20, 8.5),
        ("Luis", 22, 7.0),
        ("Marta", 19, 9.2),
        ("Pablo", 21, 6.8),
        ("Sara", 23, 8.9),
    ]
    cursor.executemany("INSERT INTO alumnos (nombre, edad, nota) VALUES (?, ?, ?)", alumnos)
    conexion.commit()
    print("✅ Datos insertados correctamente.")
else:
    print("ℹ️ La tabla ya tiene datos, saltando inserción.")

# --- PARTE NUEVA: PARA QUE SE "EJECUTE" VISUALMENTE ---

print("\n--- LISTA DE ALUMNOS EN LA BASE DE DATOS ---")
cursor.execute("SELECT * FROM alumnos")
filas = cursor.fetchall()

for fila in filas:
    print(f"ID: {fila[0]} | Nombre: {fila[1]:<10} | Edad: {fila[2]} | Nota: {fila[3]}")

# 4. Cerramos
conexion.close()