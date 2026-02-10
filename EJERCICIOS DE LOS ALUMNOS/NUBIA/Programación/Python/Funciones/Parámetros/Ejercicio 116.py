# Confeccionar una aplicación que muestre una presentación en pantalla del programa. 
# Solicite la carga de dos valores y nos muestre la suma. 
# Mostrar finalmente un mensaje de despedida del programa.

def saludar():
    print("APP DE SUMA")
    nombre = input("Ingrese su nombre: ").capitalize()
    print(f"Bienvenido/a, {nombre}")
    
def suma():
    print("Ingrese dos números para realizar la suma: ")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1 + num2  
  
def despedir():
    print("Gracias por usar el programa")
    
def main():
    saludar()
    resultado = suma()
    print(f"La suma es: {resultado}")
    despedir()
    
main()

