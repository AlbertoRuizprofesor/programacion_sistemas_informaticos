# Cargar una cadena de caracteres por teclado. 
# Mostrar la cadena del final al principio utilizando subíndices negativos.

palabra = input("Introduzca una palabra cualquiera: ")

indice = -1 

for i in range(len(palabra)):
    print(palabra[indice], end = "")
    indice -= 1 
    