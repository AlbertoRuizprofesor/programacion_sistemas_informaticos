#Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
#Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def menor_valor():
    valor1=int(input("muestra del primer valor:"))
    valor2=int(input("muestra del segundo valor:"))
    valor3=int(input("muestra del tercer valor"))
    print("menor de los tres valores")

    if valor1<valor2 and valor1<valor3:
        print(valor1)
    else: 
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)
    
#bloque principal 

menor_valor()
menor_valor()

