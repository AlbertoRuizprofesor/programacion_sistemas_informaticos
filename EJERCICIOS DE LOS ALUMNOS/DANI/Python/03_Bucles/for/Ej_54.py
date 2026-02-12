# Se cuenta con la siguiente información:Las edades de 5 estudiantes del turno mañana.Las edades de 6 estudiantes del turno tarde.Las edades de 11 estudiantes del turno noche.

sum_mañana = 0
sum_tarde = 0
sum_noche = 0

# Las edades de cada estudiante deben ingresarse por teclado.
print("Alumnos de mañana:")
for x in range(5):
    mañana = int(input(f"Ingresa la edad del alumno {x+1}: "))
    sum_mañana += mañana

print("\nAlumnos de tarde:")
for x in range(6):
    tarde = int(input(f"Ingresa la edad del alumno {x+1}: "))
    sum_tarde += tarde

print("\nAlumnos de noche:")
for x in range(11):
    noche = int(input(f"Ingresa la edad del alumno {x+1}: "))
    sum_noche += noche

# a) Obtener el promedio de las edades de cada turno (tres promedios)
promedio_mañana = sum_mañana / 5
promedio_tarde = sum_tarde / 6
promedio_noche = sum_noche / 11

# b) Imprimir dichos promedios (promedio de cada turno)
print(f"\nPromedio del turno de mañana: {promedio_mañana:.2f}")
print(f"Promedio del turno de tarde: {promedio_tarde:.2f}")
print(f"Promedio del turno de noche: {promedio_noche:.2f}\n")

# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
if promedio_mañana > promedio_noche and promedio_mañana > promedio_tarde:
    print("El turno de mañana tiene un promedio de edades mayor.")
elif promedio_mañana < promedio_tarde and promedio_noche < promedio_tarde:
    print("El turno de tarde tiene un promedio de edades mayor.")
elif promedio_mañana < promedio_noche and promedio_noche > promedio_tarde:
    print("El turno de noche tiene un promedio de edades mayor.")
else:
    print("El promedio coincide en varios turnos.")