numeros = []

while True:
    valor = input("Introduce un entero o 'fin': ")
    if valor.lower() == "fin":
        break

    try:
        numeros.append(int(valor))
    except ValueError:
        print("Valor no válido")

if numeros:
    print("Suma:", sum(numeros))
    print("Media:", sum(numeros) / len(numeros))
else:
    print("No se introdujeron números válidos")
