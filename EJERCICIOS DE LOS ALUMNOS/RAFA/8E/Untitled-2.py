nombre=input("Ingrese su nombre:")
print("Primer caracter")
print(nombre[0])
print("Cantidad de letras del nombre:")
print(len(nombre))
if len(nombre)<5:
    print("tiene menos de 5 letras")
else:
    print("tiene mas de 5 letras")