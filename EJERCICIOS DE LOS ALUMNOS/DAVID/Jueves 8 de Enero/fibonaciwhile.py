# Inicializamos los primeros valores
a = 0
b = 1

print("Serie de Fibonacci hasta el 89:")

# El ciclo continuará mientras 'a' sea menor o igual a 89
while a <= 89:
    print(a, end=" ")
    
    # Actualizamos los valores
    a, b = b, a + b