# Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. 
# La carga de los valores hacerlo por teclado.

def mayor():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    return max(valor1, valor2, valor3) #max muestra el valor mayor
print(f"El mayor es: {mayor()}")
