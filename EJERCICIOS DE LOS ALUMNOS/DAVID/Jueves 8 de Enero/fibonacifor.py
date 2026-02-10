# Pedimos la cantidad de términos
limite = int(input("¿Cuántos números de la serie de Fibonacci quieres ver?: "))

a = 0
b = 1

print(f"\nSerie de Fibonacci ({limite} términos):")

# El bucle for recorre el rango desde 0 hasta el límite solicitado
for _ in range(limite):
    print(a, end=" ")
    
    # Actualizamos los valores usando asignación múltiple
    # 'a' se convierte en el actual 'b'
    # 'b' se convierte en la suma de ambos
    a, b = b, a + b