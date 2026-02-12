print("Ejercicio 142")
print("")
print("")

def multiplicar(valor, limite=10):
    resultado = 0
    for i in range(1, limite + 1):
        resultado = valor * i
        print(valor ,"*", resultado)
    return resultado

num=int(input("Introduce el número a multiplicar: "))
multiplicar(num)

print("Fin del programa")





