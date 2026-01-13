"""
Hacer una función que me pida 5 notas y haga un promedio
"""

def media():
    suma = 0
    for i in range(5):
        nota = float(input("Introduce una nota: "))
        suma += nota
    promedio = suma / 5
    return promedio

resultado = media()
print("La media de las notas es:", resultado)



    
        
                    