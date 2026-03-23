#Pide una nota numérica entre 0 y 10 y muestra su calificación textual:
#suspenso, aprobado, bien, notable o sobresaliente.

nota = float (input ("Nota (0-10): "))
if nota < 0 or nota > 10:
    print("Error: la nota tiene que estar entre 0 y 10")
if nota < 5:
    print("suspenso")
if nota < 6:
    print("bien")
if nota < 7:
    print("aprobado")
if nota < 9:
    print("notable")
else:
    print("sobresaliente")