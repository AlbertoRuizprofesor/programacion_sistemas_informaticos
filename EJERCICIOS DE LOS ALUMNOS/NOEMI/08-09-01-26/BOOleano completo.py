#Booleano completo.

#Está mal hecho porque es un código espagetis!!!! POR PONER PRINT EN CADA OPCION.

opcion=True

while opcion:
    print("Bienvenido a la calculadora Básica")
    opcion=int(input("\nElige una opción 1:Sumar, 2:Restar, 3:Multiplicar, 4:Dividir, 5:Salir : "))
    if opcion>=1 and opcion<=4:
        eleccion1=int(input("\nIntroduce el primer valor: "))
        eleccion2=int(input("\nIntroduce el segundo valor: "))
    
    if opcion ==1: 
        suma=eleccion1+eleccion2
        print(f"Has elegido sumar, la suma de {eleccion1} y {eleccion2} es {suma} ")
    elif opcion ==2:
        resta=eleccion2-eleccion1
        print(f"Has elegido resta, la resta de {eleccion1} y {eleccion2} es {resta}")
    elif opcion ==3:
        multiplicar=eleccion1*eleccion2
        print(f"Has elegido multiplicar, la multiplicación de {eleccion1} y {eleccion2} es {multiplicar}")
    elif opcion ==4:
        dividir=eleccion1/eleccion2
        print(f"Has elegido dividir, la división de {eleccion1} y {eleccion2} es {dividir}")

    elif opcion ==5:
        print("Has elegido salir.")
        opcion=False
        
    else:
        print("Opción no válida.")    