import sqlite3

# 1. Conectar y preparar
conexion = sqlite3.connect("academia.db")
cursor = conexion.cursor()

# 2. Asegurarnos de que existan datos (por si acaso)
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    nota REAL
)
""")

# Insertamos solo si está vacía
cursor.execute("SELECT COUNT(*) FROM alumnos")
if cursor.fetchone()[0] == 0:
    datos = [("Ana", 20, 8.5), ("Luis", 22, 7.0), ("Marta", 19, 9.2), ("Pablo", 21, 6.8), ("Sara", 23, 8.9)]
    cursor.executemany("INSERT INTO alumnos (nombre, edad, nota) VALUES (?, ?, ?)", datos)
    conexion.commit()

# --- TUS CONSULTAS ---

print("--- 1. Todos los alumnos ---")
cursor.execute("SELECT * FROM alumnos")
print(cursor.fetchall())

print("\n--- 2. Alumnos con nota >= 8 (Ordenados) ---")
cursor.execute("SELECT nombre, nota FROM alumnos WHERE nota >= 8 ORDER BY nota DESC")
mejores = cursor.fetchall()
for nombre, nota in mejores:
    print(f"Estudiante: {nombre} | Nota: {nota}")

print("\n--- 3. Estadísticas ---")
cursor.execute("SELECT AVG(nota) FROM alumnos")
media = cursor.fetchone()[0]
print(f"Nota media de la clase: {media:.2f}")

conexion.close()