#Ejercicio 126: Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.


def cantidad_vocal_a(palabra):
    cantidad=0
    for i in range(len(palabra)):
        if palabra[i]=="a" or palabra[i]=="A":
            cantidad=cantidad+1
    return cantidad



palabra=input("Ingrese una palabra: ")
print(f"La palabra {palabra} tiene {cantidad_vocal_a(palabra)} a")
    