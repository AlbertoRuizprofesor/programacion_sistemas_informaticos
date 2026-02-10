"""
Se cuenta con la siguiente información:Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

"""
#Acumulador de edades del turno mañana
suma1 = 0

#Acumulador de edades del turno tarde
suma2 = 0

#Acumulador de edades del turno noche
suma3 = 0

#Ingreso de 5 edades para el turno mañana
for f in range(5):
    edad = int(input("Ingrese edad:"))
    suma1 = suma1 + edad

#Cálculo del promedio del turno mañana
promedio1 = suma1/5
print("Promedio de edades del turno mañana:")
print(promedio1)

#Ingreso de 6 edades para el turno tarde
for f in range(6):
    edad = int(input("Ingrese edad:"))
    suma2 = suma2 + edad

#Cálculo del promedio del turno tarde
promedio2 = suma2/6
print("Promedio de edades del turno tarde:")
print(promedio2)

#Ingreso de 11 edades para el turno noche
for f in range(11):
    edad = int(input("Ingrese edad:"))
    suma3 = suma3 + edad

#Cálculo del promedio del turno noche
promedio3 = suma3/11
print("Promedio de edades del turno noche:")
print(promedio3)

#Comparación para determinar qué turno tiene el promedio menor
if promedio1 < promedio2 and promedio1 < promedio3:
    print("El turno mañana tiene un promedio menor de edades.")
else:
    if promedio2 < promedio3:
        print("El turno tarde tiene un promedio menor de edades.")
    else:
        print("El turno noche tiene un promedio menor de edades.")