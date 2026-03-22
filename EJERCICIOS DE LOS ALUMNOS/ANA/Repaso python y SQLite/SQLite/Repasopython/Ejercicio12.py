#Pide repetidamente números enteros al usuario hasta que escriba fin. 
#Guarda los válidos en una lista e ignora los valores no convertibles mostrando un mensaje.

numeros = []

while true:
    valor = input("introduce un entero o 'fin' : ")
    if  valor.lower() == "fin":
    
    break

try: numeros.append(int(valor))

except ValueError:
    print("valor no valido")

if numeros: 
    print("suma: ", sum(numeros))
    print("suma: ", sum(numeros) / len (numeros))

else: 
    print("no se introdujeron numeros validos")

