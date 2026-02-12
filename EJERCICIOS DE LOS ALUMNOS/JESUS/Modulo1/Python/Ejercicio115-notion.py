#Ejercicio 115 notion Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)


def mas_peq():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero : "))
    num3=int(input("Ingrese el tercer numero: "))
    print("El numero mas pequeño de los es")

    if num1<num2 and num1<num3:
        print(num1)
    else:
        if num2<num3:
            print(num2)
        else:
            print(num3)

mas_peq()
mas_peq()