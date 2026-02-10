"""
Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc

"""

mult8 = 8   #Empezamos en 8, primer múltiplo de 8

while mult8 <= 500:     #Mientras el múltiplo no supere 500...

    if mult8 + 8 <= 500:          #Si el siguiente múltiplo sigue siendo válido...
        print(mult8, end=" - ")   #...imprimimos con guion y espacio
    else:                         #Si es el último múltiplo permitido...
        print(mult8)      #...lo imprimimos sin guion ni espacio al final
    mult8 = mult8 + 8     #Pasamos al siguiente múltiplo sumando 8



    