# Solicitamos el número al usuario y lo convertimos a entero
numero = int(input("¿De qué número quieres la tabla de multiplicar?: "))

# Inicializamos un contador en 1
i = 1

print(f"\nTabla del {numero}:")

# El bucle se ejecutará mientras 'i' sea menor o igual a 10
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
    # Es MUY importante incrementar el contador para evitar un bucle infinito
    i += 1