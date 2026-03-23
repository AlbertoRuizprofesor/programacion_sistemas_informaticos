import sqlite3

conexion = sqlite3.connect("C:\\SQLite\\academia.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM alumnos")
print(cursor.fetchall())

cursor.execute("SELECT nombre, nota FROM alumnos WHERE nota >= 8 ORDER BY nota DESC")
print(cursor.fetchall())

cursor.execute("SELECT AVG(nota) FROM alumnos")
print("Nota media:", cursor.fetchone()[0])

conexion.close()
