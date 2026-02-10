# Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
# Llamarla desde el bloque principal del programa 3 veces con string distintos.

def contar_vocales():
    palabra = input("Ingrese una palabra: ")
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador = contador + 1
    print(f"La palabra {palabra} tiene {contador} vocales.")
 
for n in range(3):
    contar_vocales()   
