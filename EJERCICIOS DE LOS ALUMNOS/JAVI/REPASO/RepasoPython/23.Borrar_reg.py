import sqlite3

# 1. Conectar
conexion = sqlite3.connect("academia.db")
cursor = conexion.cursor()

# Variables para los cambios
alumno_id = 1
nueva_nota = 9.4

# 2. ACTUALIZAR (UPDATE)
cursor.execute("UPDATE alumnos SET nota = ? WHERE id = ?", (nueva_nota, alumno_id))
print(f"✅ Filas actualizadas: {cursor.rowcount}")

# 3. BORRAR (DELETE)
# Usamos (5,) porque Python necesita una 'tupla'. La coma es obligatoria si es solo un valor.
cursor.execute("DELETE FROM alumnos WHERE id = ?", (5,))
print(f"🗑️ Filas borradas: {cursor.rowcount}")

# 4. GUARDAR CAMBIOS (¡Vital!)
conexion.commit()

# --- VERIFICACIÓN FINAL ---
print("\n--- ESTADO FINAL DE LA TABLA ---")
cursor.execute("SELECT * FROM alumnos")
for alumno in cursor.fetchall():
    print(f"ID: {alumno[0]} | Nombre: {alumno[1]:<7} | Nota: {alumno[3]}")

conexion.close()