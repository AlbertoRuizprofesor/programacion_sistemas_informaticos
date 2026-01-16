# Definir una lista con 8 elementos enteros, dichos números tendrá que introducirlos el usuario. 
# Contar cuantos de dichos valores almacenan un valor superior a 100.

# Creación de una lista vacía y variables
lista = []
x = 1
mayor_100 = 0

while x < 9 :
    num = int(input(f"Ingresa el {x}º número: "))
    lista.append(num) # Esto indica que los numeros que meta el usuario se introducirán en la lista.
    x = x + 1
    
    if num > 100:
        mayor_100 = mayor_100 + 1

if mayor_100 == 1:
    print(f"\nLa lista es {lista}.\nEn la lista se ha añadido un número mayor a 100.")
else:
    print(f"\nLa lista es {lista}.\nEn la lista se han añadido {mayor_100} números mayores a 100.")