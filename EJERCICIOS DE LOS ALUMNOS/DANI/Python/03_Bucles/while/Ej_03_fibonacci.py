# Hagamos la sucesión de Fibonacci

# Variables
x = 0
y = 1
i = 0
# Indicamos que la 'i' nos de números hasta llegar al 10 (el 0 también cuenta)
while i <= 9:
    print(f"El {i + 1}º resultado es {x}")
    x, y = y, x+y # la 'y' es el pasado y 'x+y' es el presente
    # a la izquierda del '=' está el resultado
    i += 1