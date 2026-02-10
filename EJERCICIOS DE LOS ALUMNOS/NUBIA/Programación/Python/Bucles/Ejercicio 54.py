# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

edad_mañana1 = int(input("Ingrese la edad del estudiante 1 del turno mañana: "))
edad_mañana2 = int(input("Ingrese la edad del estudiante 2 del turno mañana: "))
edad_mañana3 = int(input("Ingrese la edad del estudiante 3 del turno mañana: "))
edad_mañana4 = int(input("Ingrese la edad del estudiante 4 del turno mañana: "))
edad_mañana5 = int(input("Ingrese la edad del estudiante 5 del turno mañana: "))

edad_tarde1 = int(input("Ingrese la edad del estudiante 1 del turno tarde: "))
edad_tarde2 = int(input("Ingrese la edad del estudiante 2 del turno tarde: "))
edad_tarde3 = int(input("Ingrese la edad del estudiante 3 del turno tarde: "))
edad_tarde4 = int(input("Ingrese la edad del estudiante 4 del turno tarde: "))
edad_tarde5 = int(input("Ingrese la edad del estudiante 5 del turno tarde: "))
edad_tarde6 = int(input("Ingrese la edad del estudiante 6 del turno tarde: "))

edad_noche1 = int(input("Ingrese la edad del estudiante 1 del turno noche: "))
edad_noche2 = int(input("Ingrese la edad del estudiante 2 del turno noche: "))
edad_noche3 = int(input("Ingrese la edad del estudiante 3 del turno noche: "))
edad_noche4 = int(input("Ingrese la edad del estudiante 4 del turno noche: "))
edad_noche5 = int(input("Ingrese la edad del estudiante 5 del turno noche: "))
edad_noche6 = int(input("Ingrese la edad del estudiante 6 del turno noche: "))
edad_noche7 = int(input("Ingrese la edad del estudiante 7 del turno noche: "))
edad_noche8 = int(input("Ingrese la edad del estudiante 8 del turno noche: "))
edad_noche9 = int(input("Ingrese la edad del estudiante 9 del turno noche: "))
edad_noche10 = int(input("Ingrese la edad del estudiante 10 del turno noche: "))
edad_noche11 = int(input("Ingrese la edad del estudiante 11 del turno noche: "))

promedio_mañana = (edad_mañana1 + edad_mañana2 + edad_mañana3 + edad_mañana4 + edad_mañana5) / 5
promedio_tarde = (edad_tarde1 + edad_tarde2 + edad_tarde3 + edad_tarde4 + edad_tarde5 + edad_tarde6) / 6
promedio_noche = (edad_noche1 + edad_noche2 + edad_noche3 + edad_noche4 + edad_noche5 + edad_noche6 + edad_noche7 + edad_noche8 + edad_noche9 + edad_noche10 + edad_noche11) / 11

print(f"El promedio de edades del turno mañana es: {promedio_mañana}")
print(f"El promedio de edades del turno tarde es: {promedio_tarde}")
print(f"El promedio de edades del turno noche es: {promedio_noche}")

if promedio_mañana > promedio_tarde and promedio_mañana > promedio_noche:
    print("El turno con el mayor promedio de edades es el turno mañana.")
elif promedio_tarde > promedio_mañana and promedio_tarde > promedio_noche:
    print("El turno con el mayor promedio de edades es el turno tarde.")
else:
    print("El turno con el mayor promedio de edades es el turno noche.")
    
# ----------------------------------------------------------------------------------------------------------
#Código profesor:

suma1=0
suma2=0
suma3=0

for f in range(5):
    edad=int(input("Ingrese edad:"))
    suma1=suma1+edad
pro1=suma1/5
print("Promedio de edades del turno mañana:")
print(pro1)

for f in range(6):
    edad=int(input("Ingrese edad:"))
    suma2=suma2+edad
pro2=suma2/6
print("Promedio de edades del turno tarde:")
print(pro2)

for f in range(11):
    edad=int(input("Ingrese edad:"))
    suma3=suma3+edad
pro3=suma3/11
print("Promedio de edades del turno noche:")
print(pro3)
if pro1<pro2 and pro1<pro3:
    print("El turno mañana tiene un promedio menor de edades.")
else:
    if pro2<pro3:
        print("El turno tarde tiene un promedio menor de edades.")
    else:
        print("El turno noche tiene un promedio menor de edades.")