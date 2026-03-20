''' 
Pide repetidamente números enteros al usuario hasta que escriba fin. 
Guarda los válidos en una lista e ignora los valores no convertibles mostrando un mensaje. 
Idea clave: Al terminar, muestra la suma y la media de los números válidos. 
'''
# lista donde guardar los números pedidos al usuario
numeros = []

# bucle para pedir números al usuario hasta que escriba fin
while True:
    
    entradaNumero = input("Introduce un número entero (o 'fin' para terminar): ")
    
    if entradaNumero.lower() == 'fin':
        break
    
    try:
        numero = int(entradaNumero)
        numeros.append(numero)
        
    except ValueError:
        print("Valor no válido. Por favor, introduce un número entero.")

if numeros:
    suma = sum(numeros)
    print(f"Suma de los números válidos: {suma}")
    print(f"Media de los números válidos: {suma/len(numeros):.2f}") # media calculada directamente (sin definir variable)
    
else:
    print("No se introdujeron números válidos.")