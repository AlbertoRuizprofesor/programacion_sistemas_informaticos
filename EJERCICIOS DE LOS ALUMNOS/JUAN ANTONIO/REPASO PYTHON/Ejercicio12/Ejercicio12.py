# Ejercicio 12. Conversor robusto de números

valores = []

while True:
    entrada = input("Escribe un número entero o 'fin': ")
    if entrada.lower() == "fin":
        break

    try:
        valores.append(int(entrada))
    except ValueError:
        print("Entrada no válida")

if valores:
    print("Suma:", sum(valores))
    print("Media:", sum(valores) / len(valores))
else:
    print("No se registraron números válidos")
