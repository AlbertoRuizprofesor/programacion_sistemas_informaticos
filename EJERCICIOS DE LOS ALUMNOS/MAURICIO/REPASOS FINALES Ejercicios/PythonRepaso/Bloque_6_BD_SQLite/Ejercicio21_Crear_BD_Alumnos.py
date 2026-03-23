import sqlite3

conexion = sqlite3.connect("academia.db")
cursor = conexion.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    nota REAL
)
"""
)

alumnos = [
    ("Ana", 20, 8.5),
    ("Luis", 22, 7.0),
    ("Marta", 19, 9.2),
    ("Pablo", 21, 6.8),
    ("Sara", 23, 8.9),
]

cursor.executemany("INSERT INTO alumnos (nombre, edad, nota) VALUES (?, ?, ?)", alumnos)
conexion.commit()
conexion.close()
