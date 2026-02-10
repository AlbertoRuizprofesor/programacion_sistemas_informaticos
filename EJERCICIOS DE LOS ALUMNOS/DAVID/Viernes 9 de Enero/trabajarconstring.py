#trabajar con string
nombre1="Alberto"
posicion=nombre1[0] #primer caracter
print("caracter nº1",posicion)

if posicion>="A" and posicion<="Z":
    print("es mayuscula")
    
else:
    print("es minuscula")
    print("el numero de caracteres", len(nombre1))