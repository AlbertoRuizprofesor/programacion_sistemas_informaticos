opcion=True

while opcion:
    print("1 sumar 2 restar 3 multiplicar 4 dividir 5 salir")
    eleccion=int(input("elige una opcion"))
    if eleccion>=1 and eleccion<=4:
        
        numero1=int(input("dime el 1: "))
        numero2=int(input("dime el 2: "))
        
        if eleccion==1:
            print("elegido sumar")
            operacion="sumar"
            total=numero1+numero2
            
        elif eleccion==2:
            print("has elegido restar")
            operacion="restar"
            total=numero1-numero2
            
        elif eleccion==3:
            print("has elegido multiplicar")
            operacion="multiplicar"
            total=numero1*numero2
        elif eleccion==4:
            print("has elegido dividir")
            operacion="dividir"
            total=numero1/numero2
        print(f"operacion: {operacion}, el total es: {total}")
    if eleccion==5:
        print("saliendo")
        opcion=False
    if eleccion<=0 or eleccion>5:
        print("opcion no valida")
    
    
    
    