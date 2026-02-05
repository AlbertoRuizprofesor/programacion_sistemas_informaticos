# Problema 4: (Programa:ejercicio43.py)

suma = 0
print("A continuación va a tener que ingresar 10 valores enteros: ")
for x in range(10):
    valor = int(input("Ingrese valor:"))
    suma = suma + valor
print("La suma es")
print(suma)
promedio = suma / 10
print("El promedio es:")
print(promedio)
