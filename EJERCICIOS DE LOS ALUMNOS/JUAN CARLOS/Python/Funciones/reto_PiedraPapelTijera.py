""" 2º RETO CON FUNCIONES
 Modificar el juego, piedra papel tijeras usando funciones."""
#Librerias
import random
#Funciones
def menuInicio():
	seleccion = 0
	print(f"\n=== === === Piedra / Papel / Tijera === === ===")
	print("1.-Jugar\n2.-Salir")
	print("=== === === === === === === === === === === === ===")
	seleccion = int(input("Selecciona una opción: "))
	if seleccion >= 1 and seleccion <= 2:
		return seleccion
	else:
		print("\n*******************************************")
		print("Selección incorrecta. Vuelve a intentarlo. ")
		print("*******************************************\n")
		menuInicio()
def menuJuego():
	seleccion = 0
	print(f"\n=== === === Elije === === ===")
	print("1.-Piedra\n2.-Papel\n3.-Tijera")
	print("=== === === === === === === === === ===")
	seleccion = int(input("Selecciona una opción: "))
	if seleccion >= 1 and seleccion <= 3:
		return seleccion
	else:
		print("\n*******************************************")
		print("Selección incorrecta. Vuelve a intentarlo. ")
		print("*******************************************\n")
		menuJuego()
def ganador(usuario, maquina, listaPartidas):
	if usuario == maquina:
		print("Empate")
		listaPartidas[0]+= 1
	else:
		if ((usuario == 1 and maquina == 3) or (usuario == 2 and maquina == 1) or (usuario == 3 and maquina == 2)):
			print("Ganas")
			listaPartidas[1] += 1
		else:
			print("Pierdes")
			listaPartidas[2] += 1
	print(f"Elegiste: {usuario} la máquina eligió: {maquina}")
#Definicinición de variables.
listaPartidas = [0, 0, 0] #0.- empate, 1.-Ganadas, 2.- Perdidas
#Logica
print("\033c", end="")
while True:
	jugar = menuInicio()
	if jugar == 2:
		print("Saliendo.com")
		break
	usuario = menuJuego()
	maquina = random.randint(1, 3)
	contador = ganador(usuario, maquina, listaPartidas)
#Impresion Resultados
print("\n=== === === Resultado === === ===")
print(f"Jugaste un total de {sum(listaPartidas)} partidas:\nGanaste: {listaPartidas[1]}\nPerdiste: {listaPartidas[2]}\nEmpataste: {listaPartidas[0]}")
