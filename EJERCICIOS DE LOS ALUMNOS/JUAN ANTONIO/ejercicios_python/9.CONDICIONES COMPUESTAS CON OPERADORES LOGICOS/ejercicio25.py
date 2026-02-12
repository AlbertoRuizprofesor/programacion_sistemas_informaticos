#Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero). 
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)


# Pedimos al usuario la coordenada x e y
x=int(input("Ingrese coordenada x:"))
y=int(input("Ingrese coordenada y:"))

#Comparaciones para saber en que cuadrante se encuentra el punto

# Primer cuadrante: x positivo y y positivo
if x > 0 and y > 0:
    print("Se encuentra en el primer cuadrante")
else:
    if x < 0 and y > 0:     # Segundo cuadrante: x negativo y y positivo
        print("Se encuentra en el segundo cuadrante")
    else:
        if x < 0 and y < 0:   # Tercer cuadrante: x negativo y y negativo
            print("Se encuentra en el tercer cuadrante")
        else:   # Si no cumple ninguna de las anteriores, cae en el cuarto cuadrante
            print("Se encuentra en el cuarto cuadrante")
