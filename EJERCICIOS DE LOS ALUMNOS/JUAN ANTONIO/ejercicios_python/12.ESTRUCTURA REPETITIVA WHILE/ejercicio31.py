"""
Una planta que fabrica perfiles de hierro posee un lote de n piezas.

Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; 
sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. 
Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

"""
cantidad = int(input("¿Cuántas piezas hay en el lote?"))    #Pedimos cuántas piezas se van a procesar y lo convertimos a entero

contador = 0    #Contador para saber cuántas piezas llevamos ingresadas

aptas = 0       #Contador de piezas aptas (la que están entre 1.20 y 1.30)

while contador < cantidad:  #Repetimos el proceso tantas veces como piezas haya en el lote

    longitud = float(input("Ingresa la longitud de la pieza: "))    #Pedimos la longitud de la pieza y la convertimos a número decimal

    if 1.20 <= longitud <= 1.30:    #Si la longitud está dentro del rango permitido...
        aptas += 1      #Sumamos 1 al contador de piezas aptas

    contador += 1       #Aumentamos el contador para avanzar hacia el final del bucle

print("Cantidad de piezas aptas: ", aptas)  #Mostramos cuántas piezas cumplen con la medida correcta

