nombre1="Alberto"
posicion=nombre1[0] #Primer caracter
print(f"Caracter nº1 {posicion}")

if posicion>="A" and posicion<="Z":
    print("es mayuscula")
else:
    print("es minuscula")

print(f"El número de caracteres es {len(nombre1)}")