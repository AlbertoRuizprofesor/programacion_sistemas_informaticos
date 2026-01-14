print("Ejercicio 119")
print("")
print("")

# Definición de funciones

def solicitudtexto():
    texto=input("Ingrese un texto cualquiera: ")
    return texto

def contarvocales(cadena):
    contador=0
    for letra in cadena:
        if letra.lower() in 'aeiou':
            contador += 1
    return contador

# Programa principal

textoingresado = solicitudtexto()
numerovocales = contarvocales(textoingresado)
print("El texto ingresado tiene", numerovocales, "vocales.")
