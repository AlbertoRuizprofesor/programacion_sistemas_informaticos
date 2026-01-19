"""

"""




#Contadores para cada cuadrante del plano cartesiano
puntos_cuadrante1 = 0
puntos_cuadrante2 = 0
puntos_cuadrante3 = 0
puntos_cuadrante4 = 0 

#Pedimos cuántos puntos se van a ingresar
n=int(input("Cantidad de puntos:"))

#Repetimos el proceso "n" veces
for f in range(n):
    #Pedimos las coordenadas del punto
    x=int(input("Ingrese coordenada x:"))
    y=int(input("Ingrese coordenada y:"))

    #Primer cuadrante: x positivo y positivo
    if x > 0 and y > 0:
        puntos_cuadrante1 = puntos_cuadrante1 + 1
    else:   #Segundo cuadrante x negativo y positivo
        if x < 0 and y > 0:
            puntos_cuadrante2 = puntos_cuadrante2 + 1  
        else:   #Tercer cuadrante x negativo y negativo
            if x < 0 and y < 0:
                puntos_cuadrante3 = puntos_cuadrante3 + 1
            else:   #Cuarto cuadrante x positivo y negativo
                if x > 0 and y < 0:
                    puntos_cuadrante4 = puntos_cuadrante4 + 1
                    
#Mostramos cuántos puntos cayeron en cada cuadrante
print("Cantidad de puntos en el primer cuadrante:", puntos_cuadrante1)

print("Cantidad de puntos en el segundo cuadrante:", puntos_cuadrante2)

print("Cantidad de puntos en el tercer cuadrante:",puntos_cuadrante3)

print("Cantidad de puntos en el cuarto cuadrante:", puntos_cuadrante4)
