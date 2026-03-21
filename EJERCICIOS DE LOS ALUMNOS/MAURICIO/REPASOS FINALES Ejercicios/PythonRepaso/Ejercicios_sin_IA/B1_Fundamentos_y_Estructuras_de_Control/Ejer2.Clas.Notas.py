# Ejercicio 2. Clasificador de notas
# Pide una nota numérica entre 0 y 10 y muestra su calificación textual:
# suspenso, aprobado, bien, notable o sobresaliente.
# Ampliación: Si la nota está fuera de rango, informa del error.

nota = float(input("Dime tu nota del examen entre 0 y 10: "))

if nota == 0:
    print("\nA la carcel!!!\n")
elif nota < 5:
    print("\nSuspenso!!!\n")
elif nota < 6:
    print("\naprobado raspado!!!\n")
elif nota < 7:
    print("\nBien!!!\n")
elif nota < 8:
    print("\nNotable!!!\n")
elif nota < 10:
    print("\nsobresaliente!!!\n")
elif nota == 10:
    print("\nEres un Crack!!!\n")
