# Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.

def contar_a(string):
    contador = 0
    for letra in string:
        if letra == "a" or letra == "A":
            contador = contador + 1
    return contador

string = input("Ingrese una palabra: ")
print(f"La palabra {string} tiene {contar_a(string)} letras 'a' o 'A'.")

