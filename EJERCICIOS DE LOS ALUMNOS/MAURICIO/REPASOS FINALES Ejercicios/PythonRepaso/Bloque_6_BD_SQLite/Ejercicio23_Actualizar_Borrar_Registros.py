import sqlite3

conexion = sqlite3.connect("academia.db")
cursor = conexion.cursor()

alumno_id = 1
nueva_nota = 9.4

cursor.execute("UPDATE alumnos SET nota = ? WHERE id = ?", (nueva_nota, alumno_id))
print("Filas actualizadas:", cursor.rowcount)

cursor.execute("DELETE FROM alumnos WHERE id = ?", (5,))
print("Filas borradas:", cursor.rowcount)

conexion.commit()
conexion.close()
