"""
- Cargar una cadena por teclado luego:
1) Imprimir los dos primeros caracteres.
2) Imprimir los dos últimos
3) Imprimir todos menos el primero y el último carácter.
"""
# Se solicita al usuario que escriba una cadena de texto
texto = input("Introduce una cadena de caracteres: ")

# Mostramos los dos primeros caracteres usando slicing
print("Primeros dos caracteres:")
print(texto[:2])

# Mostramos los dos últimos caracteres usando índices negativos o cálculo de longitud
print("Últimos dos caracteres:")
print(texto[len(texto) - 2:])

# Mostramos todos los caracteres excepto el primero y el último
print("Texto sin el primer y el último carácter:")
print(texto[1:len(texto) - 1])


