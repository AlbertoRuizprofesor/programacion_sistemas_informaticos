# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

alturas = []
for persona in range(5):
    altura = float(input("Ingrese la altura de la persona {}: ".format(persona + 1)))
    alturas.append(altura)

promedio = sum(alturas) / len(alturas)
mayores = 0
menores = 0

for altura in alturas: # "para cada altura en alturas"
    if altura > promedio:
        mayores += 1
    else:
        menores += 1

print(f"Alturas ingresadas: {alturas}")
print(f"Promedio de alturas: {promedio}")
print(f"Personas mayores al promedio: {mayores}")
print(f"Personas menores al promedio: {menores}")
