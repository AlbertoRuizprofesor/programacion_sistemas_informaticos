#Ejercicio de calculadora con funcion def: 

def presentacion():
    print("Bienvenido a la calculadora básica:")
    print("************************************")
    
def eleccion():
    opcion=int(input("Elige una opción (1:Sumar/ 2:Restar /3:Multiplicar/ 4:Dividir): "))
    print("Usted ha elegido ", opcion)
    return opcion
    
def valor(opcion):
    
    if opcion<1 or opcion>4:
        print("No válido.")
        return None, None
    
    num1=float(input("Introduce el primer valor: "))
    num2=float(input("Introduce el segundo valor: "))

    if opcion==1:
        total=num1+num2
        tipo="Sumar"
    
    elif opcion==2:
        total=num1-num2
        tipo="Resta"
        
    elif opcion==3:
        total=num1*num2
        tipo="Multiplicar"
        
    elif opcion==4:
        if num2==0:
            return "Dividir", "Error: no se puede dividir entre 0."
        total=num1/num2
        tipo="Dividir"
    return tipo, total

    
        
presentacion()
opcion=eleccion()
tipo, total=valor(opcion)

if tipo is None:
    print("opción no válida.")
else:
    print(f"Usted ha elegido {tipo} y su resultado es {total}")

        
    


