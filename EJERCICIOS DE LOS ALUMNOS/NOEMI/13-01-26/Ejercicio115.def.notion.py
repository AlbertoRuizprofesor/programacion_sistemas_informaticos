# Ejercico 115: Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def valor_menor():
    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    valor3=int(input("Introduce el tercer valor: "))
    
    print("Menor de los tres")

    if valor1<valor2 and valor1<valor3:
        print("El valor menor es", valor1)
    elif valor2<valor1 and valor2<valor3:
        print("El valor menor es ", valor2)
    else:
        print("El valor menor es ", valor3)
        
valor_menor()
valor_menor()

        

        
   