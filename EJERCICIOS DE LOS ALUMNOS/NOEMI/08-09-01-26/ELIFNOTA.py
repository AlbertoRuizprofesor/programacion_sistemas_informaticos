#Ejercicio con ELIF.

nota=float(input("Introduzca su nota: "))

if nota>= 8 and nota<=10:
    print("Sobresaliente")
elif nota>= 4.6 and nota<=7.9:
    print("Aprobado")
elif nota<=8:
    print("Notable")
else:
    print("suspenso")