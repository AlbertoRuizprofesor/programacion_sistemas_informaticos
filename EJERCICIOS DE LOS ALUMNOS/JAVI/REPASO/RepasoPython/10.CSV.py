import csv

alumnos = [
    ["Ana", 20, 8.5],
    ["Luis", 22, 7.0],
    ["Marta", 19, 9.2],
]

with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "edad", "nota"])
    escritor.writerows(alumnos)

notas = []
with open("alumnos.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        notas.append(float(fila["nota"]))

print("Nota media:", sum(notas) / len(notas))
