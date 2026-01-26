#Ejercicio 117 notion define una funcion con la comparativa y luego la invoca en otra que pide los valores por consola


def mostrar_mayor(v1,v2,v3): #funcion comparativa
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar(): #funcion que pide los valores por consola
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)#invocacion de la primera funcion 


# programa principal

cargar() #al incluir una funcion en otra solo invocamos la segunda 
