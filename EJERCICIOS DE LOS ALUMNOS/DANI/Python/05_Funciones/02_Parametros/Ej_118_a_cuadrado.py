# Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

# ---------FUNCIONES---------
def perimetro(n):
    perim = n * 4
    print(f"Siendo los lados {n}cm, su perímetro es {perim}")

def superficie(n):
    sup = n ** 2
    print(f"Siendo los lados {n}cm, su superficie es {sup}")

def menu():
    boolean = True
    
    #Bucle while para hacer todos los cuadrados que se quiera
    while boolean:
        lado = int(input("¿Cuánto mide un lado? "))
        
        print("Opciones:\n1. Perímetro\n2. Superficie")
        opcion1 = int(input("¿Qué quieres calcular? "))
        
        if opcion1 == 1:
            perimetro(lado)
        elif opcion1==2:
            superficie(lado)
        else:
            print("Opción no valida")
        
        # Preguntar al usuario si quiere seguir haciendo o detener el programa
        opcion2 = input("\n¿Calculamos otro cuadrado? ('S'/'N'): \n")
        if opcion2.upper() == "N":
            boolean = False

# ---------PROGRAMA PRINCIPAL---------
menu()