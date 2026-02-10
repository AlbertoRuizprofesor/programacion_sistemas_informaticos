def presentacion():
    print("Hola, bienvenido a este pequeño programa")
    
def suma(): #Ejemplo de función con input
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"La suma es: {num1 + num2}")

def finalizacion():
    input("Presione cualquier tecla + Enter para salir: ")

presentacion()
suma()
finalizacion()

