# Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
def menor():
    num1 = int(input("Dame el primer número: "))
    num2 = int(input("Dame el segundo número: "))
    num3 = int(input("Dame el tercer número: "))

    menor_numero = min(num1, num2, num3)
    print(f"El número más pequeño es {menor_numero}\n")

# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
for x in range(2):
    print(f"Llamada número {x+1}:")
    menor()