#Guarda en un archivo CSV una lista de alumnos con nombre, edad y nota. Después lee el archivo y calcula la nota media.

import csv

alumnos = [
    ["Lorena", 17, 7.5],
    ["Carlos", 20, 8.5],
    ["Raúl", 18, 6,2],

]

with open (" alumnos.csv", "w", newline = "" encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "edad", "nota"])
    escritor.writerows(alumnos)

notas = []
with open("alumnos.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        notas.append(float(fila["nota"]))

print("Nota media:", sum(notas) / len(notas))