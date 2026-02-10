opcion=True
while opcion:
    print("1 sumar 2 restar 3 multiplicar 4 dividir 5 salir")
    eleccion=int(input("elige una opcion:"))
    if eleccion>=1 and eleccion<=4:
        num1= int(input("Introduce el primer número: "))
        num2= int(input("Introduce el segundo número: "))
        if eleccion==1:
            print("Has elegido sumar: ")
            operacion="Sumar" 
            total=num1+num2
        elif eleccion==2:
            print("Has elegido restar") 
            operacion="Restar"
            total=num1-num2
        elif eleccion==3:
            print("Has elegido multiplicar") 
            operacion="Multiplicar"
            total=num1*num2    
        elif eleccion==4:
            print("Has elegido dividir") 
            operacion="Dividir"
            total=num1/num2
        print(f"La operación es: {operacion}, el total es: {total}")    
    if eleccion==5:
        print("saliendo")
        opcion=False
    if eleccion<0 or eleccion>5:
        print("Opción no válida")      