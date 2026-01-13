# Solicitamos los tres números
n1 = float(input("numero1: "))
n2 = float(input("numero2: "))
n3 = float(input("numero3: "))

# Lógica para encontrar el mayor
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

# Mostramos el resultado (usando :.0f para que se vea como en tu ejemplo)
print(f"\nel numero mayor es {mayor:.0f}")