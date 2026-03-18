# Ejercicio 10. Registro de alumnos en CSV

import csv

estudiantes = [
    ["Carlos", 21, 7.8],
    ["Elena", 23, 8.9],
    ["Pablo", 20, 6.5],
]

# Escritura del archivo CSV
with open("estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(["nombre", "edad", "nota"])
    escritor_csv.writerows(estudiantes)

# Lectura del archivo CSV
calificaciones = []
with open("estudiantes.csv", "r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)
    for registro in lector_csv:
        calificaciones.append(float(registro["nota"]))

print("Nota media:", sum(calificaciones) / len(calificaciones))
