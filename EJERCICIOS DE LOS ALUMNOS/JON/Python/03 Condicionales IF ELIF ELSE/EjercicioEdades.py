print("")
print("Ejercicio Edades")
print("")

edad=int(input("Introduce tu edad: "))

if edad<0 or edad>=120:
    print("Estás morío")
else:
	if edad>=0 and edad<3:
    	print("Eres un Bebecito pequeñito")
    if edad >=3 and edad<10:
        print("Eres un niño")
    if edad >=10 and edad<13:
        print("Eres preadolescente.")
    if edad >=13 and edad<=17:
        print("Eres adolescente")
    if edad >=18 and edad<67:
        print("Eres un trabajador")
    if edad >=67:
		print("Eres un yayo jubilado")
