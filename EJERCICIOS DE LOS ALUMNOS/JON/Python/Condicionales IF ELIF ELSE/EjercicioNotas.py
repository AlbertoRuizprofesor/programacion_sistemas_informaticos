

print("Ejercicio Notas")
nota=float(input("Ingrese su nota:"))
if 0<nota<4.5:
    print("Estás suspenso!!!")
else:
    if nota<=4.6:
        print("Has aprobado")
    if 5.6<=nota<=6.5:
        print("Tienes un bien!!!")
    if 6.6<=nota<=8.4:
        print("Pedazo Notable!!!")
    else:
    	if 8.5<=nota<=10:
        	print("Sobresaliente")
