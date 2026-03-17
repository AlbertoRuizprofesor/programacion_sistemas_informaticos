nombre = input("Su nombre, please: ")
posicion = nombre[0]
print(f"El 1º caracter es: {posicion}")

if posicion >= "A" and posicion <= "Z":
    print(f"{posicion} es mayusculas")
else:
    print(f"{posicion} es minusculas")
