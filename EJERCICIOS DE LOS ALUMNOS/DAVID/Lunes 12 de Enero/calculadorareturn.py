def presentacion():
    print("*******************************")
    print(" CALCULADORA")
    print(" Elija: 1(Suma), 2(Resta), 3(Multi), 4(Div)")
    print("*******************************")

# Funciones que retornan el valor procesado
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error (División por cero)"

def finalizacion():
    print("*******************************")
    print("Gracias por utilizar este programa")

# --- Programa Principal ---

presentacion()

opcion = input("Operación: ")
v1 = int(input("Primer valor: "))
v2 = int(input("Segundo valor: "))

# Guardamos el valor devuelto por las funciones en una variable 'resultado'
if opcion == "1":
    resultado = sumar(v1, v2)
elif opcion == "2":
    resultado = restar(v1, v2)
elif opcion == "3":
    resultado = multiplicar(v1, v2)
elif opcion == "4":
    resultado = dividir(v1, v2)
else:
    resultado = "Opción no válida"

# Mostramos el paquete que nos devolvió el return
print("El resultado final es:", resultado)

finalizacion()