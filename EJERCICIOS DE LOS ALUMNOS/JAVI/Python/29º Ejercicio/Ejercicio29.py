opcion = True

while opcion:
    print("1 sumar | 2 restar | 3 multiplicar | 4 dividir | 5 salir")
    eleccion = int(input("Elige una opcion: "))

    if eleccion >= 1 and eleccion <= 4:
        print("Has elegido: " , eleccion)
        for f in range(1):
            num1=float(input("Ingrese un valor:"))
            num2=float(input("Ingrese otro valor:"))
        
        if eleccion == 1:
            print(num1 + num2)
        if eleccion == 2:
            print(num1 - num2)
        if eleccion == 3:
            print(num1 * num2)
        if eleccion == 4:
            print(num1 / num2)      
 
    if eleccion == 5:
        opcion = False
        print ("Saliendo")

    if eleccion < 0 or eleccion > 5:
        print("Opcion no valida")
        


    
        
 
    """if eleccion==1:
       for f in range(1):
            num1=int(input("Ingrese un valor:"))
            num2=int(input("Ingrese otro valor:"))
            print("La suma es: " , (num1 + num2))
    elif eleccion==2:
        for f in range(1):
            num3=float(input("Ingrese un valor:"))
            num4=float(input("Ingrese otro valor:"))
            print("La resta es: " , (num3 - num4))
    elif eleccion==3:
        for f in range(1):
            num3=float(input("Ingrese un valor:"))
            num4=float(input("Ingrese otro valor:"))
            print("La multiplicacion es: " , (num3 * num4))
    elif eleccion==4:
        for f in range(1):
            num3=float(input("Ingrese un valor:"))
            num4=float(input("Ingrese otro valor:"))
            print("La division es: " , (num3 / num4))    
    elif eleccion==5:
        print("saliendo")
        opcion = False
    else:
        print("Opción no válida")"""




    
    
       


