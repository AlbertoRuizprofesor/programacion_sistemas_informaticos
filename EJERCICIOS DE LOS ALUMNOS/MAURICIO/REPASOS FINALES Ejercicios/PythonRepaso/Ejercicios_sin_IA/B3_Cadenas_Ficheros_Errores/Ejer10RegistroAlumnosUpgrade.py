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
    # Extraemos todas las notas en una sola línea
    notas = [float(fila["nota"]) for fila in lector]

media = sum(notas) / len(notas) if notas else 0
print(f"Nota media: {media:.2f}")
