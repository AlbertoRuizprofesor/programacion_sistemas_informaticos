# Hagamos la sucesión de Fibonacci

# Variables
x, y = 1, 2

# Indicamos que la 'i' nos de números hasta llegar al 10 (el 0 también cuenta)
for i in range(10):
    print(f"El {i + 1}º resultado es {x}")
    x, y = y, x+y # la 'y' es el pasado y 'x+y' es el presente
    # a la izquierda del '=' está el resultado