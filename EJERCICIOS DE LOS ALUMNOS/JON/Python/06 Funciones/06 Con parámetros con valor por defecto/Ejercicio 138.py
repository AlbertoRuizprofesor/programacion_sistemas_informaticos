print("Ejercicio 138")
print("")
print("")

# Confeccionar una función que reciba un string como parámetro y 
# en forma opcional un segundo string con un caracter. La función debe mostrar 
# el string subrayado con el caracter que indica el segundo parámetro.

def subrayar_texto(texto, caracter='_'):
    print(texto)
    print(caracter * len(texto))

# Ejemplo de uso
subrayar_texto("Hola Mundo")
subrayar_texto("Python es genial", '*')

print("Fin del programa")