nota = float(input("Nota (0-10): "))

if nota < 0 or nota > 10:
    print("Error: la nota debe estar entre 0 y 10")
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
