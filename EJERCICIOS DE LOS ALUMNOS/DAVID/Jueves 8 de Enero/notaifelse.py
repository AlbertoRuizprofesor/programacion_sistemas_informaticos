# Solicitamos la nota al usuario y la convertimos a número decimal
nota = float(input("Introduce la nota obtenida: "))

# Estructura de control para evaluar la nota
if nota >= 90:
    print("Sobresaliente")
elif nota >= 80:
    print("Notable")
elif nota >= 70:
    print("Aprobado")
else:
    print("Suspenso")