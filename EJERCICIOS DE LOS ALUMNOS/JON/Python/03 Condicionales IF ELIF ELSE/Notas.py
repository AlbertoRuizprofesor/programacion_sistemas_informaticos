print("Ejercicio Notas")
print("")
print("")

nota=float(input("introduce tu nota: "))

if nota>=4.5:
    print("Estás aprobado.")
    
else:
    print("Estás suspenso.")
    
if 10>nota<0:
    print("Nota no válida")
else:
    if 0>nota>4.4:
        print("Suspenso.")    
    if 4.5<nota<5.5:
        print("Aprobado.")
    if 5.5<nota<6.5:
        print("Bien.")
    if 6.6<nota<8.4:
        print("Notable.")
    if 8.5<nota<10:
        print("Sobresaliente.")