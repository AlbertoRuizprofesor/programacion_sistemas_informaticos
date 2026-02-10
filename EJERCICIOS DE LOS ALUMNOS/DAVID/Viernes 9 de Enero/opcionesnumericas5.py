opcion=True
while opcion:
    print("1 sumar 2 restar 3 multiplicar 4 dividir 5 salir")
    eleccion=int(input("elige una opcion: "))
    if eleccion>=1 and eleccion<=4:
        numero1=int(input("dime el numero 1: "))
        numero2=int(input("dime el numero 2: "))
        if eleccion==1:
            print("has elegido sumar")
            operacion="Sumar"
            total=numero1+numero2
        elif eleccion==2:
            print("has elegido restar")
            operacion="Restar"
            total=numero1-numero2
        elif eleccion==3:
              print("has elegido multiplicar")
              operacion="Multiplicar"
              total=numero1*numero2
        elif eleccion==4:
              print("has elegido dividir")
              operacion="Dividir"
              total=numero1/numero2
    if eleccion==5:
             print("saliendo")
             operacion="Salir"
             total=0
             opcion=False
    if eleccion<0 or eleccion>5:
        print("opcion no valida")
        
    print(f"La operacion es: {operacion}, el total es: {total}")
