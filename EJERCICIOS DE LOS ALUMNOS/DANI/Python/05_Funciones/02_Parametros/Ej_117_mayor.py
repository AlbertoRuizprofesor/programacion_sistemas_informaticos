# Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.
def mayor():
    num1 = int(input("Dame el primer número: "))
    num2 = int(input("Dame el segundo número: "))
    num3 = int(input("Dame el tercer número: "))

    mayor_numero = max(num1, num2, num3)
    print(f"El número más pequeño es {mayor_numero}\n")

# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
for x in range(2):
    print(f"Llamada número {x+1}:")
    mayor()