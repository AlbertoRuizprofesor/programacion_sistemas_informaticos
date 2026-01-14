# calculadora

def sumar(n1, n2):
    return "suma", n1 + n2

def resta(n1, n2):
    return "resta", n1 - n2

def mult(n1, n2):
    return "multiplicación", n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "división", "Error: división por cero"
    return "división", n1 / n2


n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))

cal = int(input("¿Qué operación quieres hacer? 1:suma 2:resta 3:mult 4:dividir → "))

match cal:
    case 1:
        operacion, resultado = sumar(n1, n2)
    case 2:
        operacion, resultado = resta(n1, n2)
    case 3:
        operacion, resultado = mult(n1, n2)
    case 4:
        operacion, resultado = dividir(n1, n2)
    case _:
        operacion = "ninguna"
        resultado = "Opción no válida"

print(f"La {operacion} es: {resultado}")
