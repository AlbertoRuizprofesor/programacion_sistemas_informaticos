#Ejercicio 18:Se cuenta con la siguiente información:Las edades de 5 estudiantes del turno mañana.Las edades de 6 estudiantes del turno tarde.Las edades de 11 estudiantes del turno noche.Las edades de cada estudiante deben ingresarse por teclado.
#a) Obtener el promedio de las edades de cada turno (tres promedios)
#b) Imprimir dichos promedios (promedio de cada turno)
#c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

suma1=0
suma2=0
suma3=0


for i in range(5):
    Edad1=int(input(f"Introduce su {i+1} edad (Turno de mañana): "))
    suma1=suma1+Edad1
    promedio1=suma1/5
print("Promedio de edades del turno de mañana", promedio1)
for i in range(6):
    Edad2=int(input(f"Introduce su {i+1} edad (Turno de tarde): "))
    suma2=suma2+Edad2
    promedio2=suma2/6
print("El promedio de las edades del turno de tarde es: ", promedio2)
for i in range(11):
    Edad3=int(input(f"Introduce su {i+1} edad (Turo de noche: )"))
    suma3=suma3+Edad3
    promedio3=suma3/11
print("El promedio de las edades de tarde es: ", promedio3)
    
if promedio1>promedio2:
    print(f"Promedio mayor es el turno de mañana {promedio2:.2f}")
elif promedio1<promedio2:
    print(f"El promedio mayor es el turno de tarde {promedio2:.2f}")
else:
    print(f"El promedio mayor es el turno de noche {promedio3:.2f}")
    