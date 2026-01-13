# Variables
x = 1 # Para iniciar el bucle while
suma = 0 # Guardar la suma de las notas
notas = [] # Lista para guardar las notas

# Inicio del bucle while
while x < 5:
    # Pedir las notas
    nota = float(input(f"Dame la {x}º nota: "))
    # Ver si es una nota real
    if nota >=0 and nota <= 10:
        # Añadir la nota a una lista
        notas.append(nota)
        # Sumar la nota añadida a la suma de las notas anteriores
        suma = nota + suma
        # +1 a x para cuando x sea 4 salgamos del bucle
        x = x + 1
    else:
        print(f"{nota} no es una nota válida.")

# Hacer la media de las notas
media = suma / 4

# Imprimir el resultado por pantalla
print(f"\nLas notas son {notas}\nLa media de las notas es {media:.2f}")