import sqlite3 
 
conexion = sqlite3.connect("C:\\SQLite\\biblioteca.db") 
cursor = conexion.cursor() 
 
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS alumnos ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre TEXT NOT NULL, 
    edad INTEGER, 
    nota REAL 
) 
""") 
 
alumnos = [ 
    ("Ana", 28, 8.5), 
    ("Noemí", 28, 9), 
    ("Nubia", 20, 9.2), 
    ("Darío", 17, 9), 
    ("Andrés", 18, 8.9), 
] 
 
cursor.executemany("INSERT INTO alumnos (nombre, edad, nota) VALUES (?, ?, ?)", alumnos) 
conexion.commit() 
conexion.close() 