# Pedimos los valores al principio como en tu ejemplo
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
print("-------------------------------")

# --- BLOQUE DE FUNCIONES QUE IMPRIMEN (Tipo 1) ---
def sumar(n1, n2):
    resultado = n1 + n2
    print(f"El resultado de la suma es: {resultado}")

def restar(n1, n2):
    resultado = n1 - n2
    print(f"El resultado de la resta es: {resultado}")

def multiplicar(n1, n2):
    resultado = n1 * n2
    print(f"El resultado de la multiplicación es: {resultado}")

def dividir(n1, n2):
    if n2 != 0:
        resultado = n1 / n2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("No se puede dividir por cero.")

# --- BLOQUE DE FUNCIONES CON RETURN (Tipo 2) ---
def sumar2(n1, n2):
    return n1 + n2

def restar2(n1, n2):
    return n1 - n2

def multiplicar2(n1, n2):
    return n1 * n2

def dividir2(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error (División por cero)"

# --- EJECUCIÓN ---

# 1. Usando las funciones que imprimen directamente
print("EJECUCIÓN DIRECTA (PRINT):")
sumar(numero1, numero2)
restar(numero1, numero2)
multiplicar(numero1, numero2)
dividir(numero1, numero2)

print("-------------------------------")

# 2. Usando las funciones con return y guardando en variables
print("EJECUCIÓN CON RETURN Y VARIABLE:")
res_suma = sumar2(numero1, numero2)
res_resta = restar2(numero1, numero2)
res_multi = multiplicar2(numero1, numero2)
res_div = dividir2(numero1, numero2)

print(f"La suma es: {res_suma}")