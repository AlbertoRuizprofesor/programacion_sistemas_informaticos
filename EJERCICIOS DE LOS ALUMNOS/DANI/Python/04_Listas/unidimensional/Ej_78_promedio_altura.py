# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas. 
# Contar cuántas personas son más altas que el promedio y cuántas más bajas.

alturas = []
suma = 0
altas = 0
bajas = 0
igual = 0

for x in range(5):
    altura = float(input(f"Ingresa altura de la persona num {x+1}: "))
    alturas.append(altura)
    suma += altura

promedio = suma / 5

for altura in alturas:
    if altura > promedio:
        altas += 1
    elif altura < promedio:
        bajas += 1
    else:
        igual += 1

print(f"Alturas ingresadas: {alturas}")
print(f"El promedio de las alturas es {promedio:.2f}")
print(f"Personas más altas que el promedio: {altas}")
print(f"Personas más bajas que el promedio: {bajas}")
print(f"Personas con altura igual al promedio: {igual}")