
while True:
    numero = int(input("Indica el número del que quieres la tabla de multiplicar: "))

    for n in range(1, 11):
        print(f"{numero} x {n} = {numero*n}")
    
    salir = input("¿Desea salir? (s/n): ").lower()
    if salir == "s":
        break
    elif salir == "n":
        pass
    else: 
        print("Selecciona una opción válida (s/n): ")