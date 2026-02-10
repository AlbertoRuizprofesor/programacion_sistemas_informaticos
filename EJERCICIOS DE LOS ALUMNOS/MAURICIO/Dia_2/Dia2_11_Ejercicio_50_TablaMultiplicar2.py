tabla = int(input("Elige la tabla de multiplicar de un número que te guste: "))
print(f" TABLA DEL {tabla}")

for i in range(1, 13):
    resultado = tabla * i
    print(f"{tabla} X {i} = {resultado}")
