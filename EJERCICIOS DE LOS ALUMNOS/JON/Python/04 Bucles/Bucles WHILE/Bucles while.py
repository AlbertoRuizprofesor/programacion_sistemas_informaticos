print("Bucles While")
print("")
print("")

opcion=True
while opcion:
    print("1 sumar 2 restar 3 multiplicar 4 dividir 5 salir")
    eleccion=int(input("Elige una opcion: "))
    if 1<=eleccion<=4:
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        if eleccion==1:
            operacion="Sumar"
            total=numero1+numero2
        elif eleccion==2:
            operacion="Restar"
            total=numero1-numero2
        elif eleccion==3:
            operacion="Multiplicar"
            total=numero1*numero2
        elif eleccion==4:
            operacion="Dividir"
            total=numero1/numero2
        print("Has elegido ", operacion, "Y el resultado es", total)
    elif eleccion==5:
        print("Has elegido salir")
        opcion=False
    else:
        print("Opcion no valida")
    
print("Fin del programa")
