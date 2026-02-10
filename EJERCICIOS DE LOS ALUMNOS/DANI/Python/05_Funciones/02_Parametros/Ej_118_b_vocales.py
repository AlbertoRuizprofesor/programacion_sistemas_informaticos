# Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.

# ---------FUNCIONES---------
def cantidad_vocales(palabra):
    cant_a = 0
    cant_e = 0
    cant_i = 0
    cant_o = 0
    cant_u = 0
    
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=='A':
            cant_a += 1
        elif palabra[x]=='e' or palabra[x]=='E':
            cant_e += 1
        elif palabra[x]=='i' or palabra[x]=='I':
            cant_i += 1
        elif palabra[x]=='o' or palabra[x]=='O':
            cant_o += 1
        elif palabra[x]=='u' or palabra[x]=='U':
            cant_u += 1

    print(f"Palabra: {palabra}")
    print(f"Cantidad 'a/A': {cant_a}")
    print(f"Cantidad 'e/E': {cant_e}")
    print(f"Cantidad 'i/I': {cant_i}")
    print(f"Cantidad 'o/O': {cant_o}")
    print(f"Cantidad 'u/U': {cant_u}\n")

# ---------PROGRAMA PRINCIPAL---------
for x in range(3):
    palabra = input("Dime una palabra / frase: ")
    cantidad_vocales(palabra)