#Ejercicio 17: Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.

def carga_valor():
    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    valor3=int(input("Introduce el tercer valor: "))
    
    print("Muesta el numero mayor")
    
    if valor1>valor2 and valor1>valor3:
        print("El valor mayor es ", valor1)
    elif valor2>valor1 and valor2>valor3:
        print("El valor mayor es ", valor2)
    else:
        print("El valor mayor es ", valor3)
        
carga_valor()


#ESTE ES OTRO PROGRAMA DEL PROFESOR:


def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)


# programa principal

cargar()
