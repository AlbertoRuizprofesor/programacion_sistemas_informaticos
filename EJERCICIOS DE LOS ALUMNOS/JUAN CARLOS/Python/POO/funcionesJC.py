"""
Funciones JC para todos los ejercicios.
"""
#Funciones
def borrarPantalla():
	print("\033c", end="")

def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def entradaDatos(numeroValores):
    for cntValores in range (numeroValores):
        #Objeto de salida
        listaValores = []
        listaValores.append(float(input(f"Introduce el valor {cntValores + 1}: ")))
        return listaValores

def menuInicio(tituloMenu = ""):
	seleccion = 0
	print(f"\n=== === === {tituloMenu} === === ===")
	print("1.-Cargar Alumnos\n2.-listar Alumnos\n3.-Alumnos notas > 7\n4.-Salir")
	print("=== === === === === === === === === ===")
	seleccion = int(input("Selecciona una opción: "))
	if seleccion >= 1 and seleccion <= 4:
		return seleccion
	else:
		print("\n*******************************************")
		print("Selección incorrecta. Vuelve a intentarlo. ")
		print("*******************************************\n")
		menuInicio()

