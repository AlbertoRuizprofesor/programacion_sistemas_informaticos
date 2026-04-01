''' 
Guarda en un archivo CSV una lista de alumnos con nombre, edad y nota. 
Después lee el archivo y calcula la nota media. 
'''

import csv

# Guardar la lista de alumnos en un archivo CSV (usando diccionarios)
alumnos = [
    {"nombre": "Nubia", "edad": 20, "nota": 10},
    {"nombre": "Noemí", "edad": 28, "nota": 9.8},
    {"nombre": "Ana", "edad": 28, "nota": 9.7}
]

with open("alumnos.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["nombre", "edad", "nota"])
    writer.writeheader()
    writer.writerows(alumnos)

# Leer el archivo y calcular la nota media
with open("alumnos.csv", "r") as file:
    reader = csv.DictReader(file)
    notas = [float(row["nota"]) for row in reader]
    nota_media = sum(notas) / len(notas)

print(f"La nota media es: {nota_media:.2f}")