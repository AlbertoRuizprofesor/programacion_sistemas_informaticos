# Ejercicio 2 Clasificador de notas
nota = float(input("Introduzca la nota: "))

if nota < 0:
    print("La nota debe estar entre 0 y 10")
elif nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Aprobado")
elif nota < 7:
    print("Bien")
elif nota < 9: 
    print("Notable")
else:
    print("Sobresaliente")

