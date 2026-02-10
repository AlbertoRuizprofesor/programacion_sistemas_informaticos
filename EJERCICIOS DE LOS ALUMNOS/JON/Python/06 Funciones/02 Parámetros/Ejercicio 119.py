print("Ejercicio 113")
print("")
print("")


def introducir_datos():
    print("Programa que permite cargar tres valores por teclado.")
    v1=int(input("Ingrese el primer valor entero: "))
    v2=int(input("Ingrese el segundo valor entero: "))
    v3=int(input("Ingrese el tercer valor entero: "))
    menor_a_mayor(v1, v2, v3)
   
def menor_a_mayor(a,b,c):
    lista = [a,b,c]
    lista.sort(reverse=False)
    print("Los números ordenados de mayor a menor son: ", lista)


#inicio del programa

introducir_datos()


print("Fin del programa")



