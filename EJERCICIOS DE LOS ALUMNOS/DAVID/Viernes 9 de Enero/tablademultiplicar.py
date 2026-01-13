# Solicitamos al usuario el número de la tabla
numero = int(input("¿De qué número quieres ver la tabla de multiplicar?: "))

print(f"\nTabla del {numero}:")
print("-" * 15)

# El ciclo for recorrerá del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")