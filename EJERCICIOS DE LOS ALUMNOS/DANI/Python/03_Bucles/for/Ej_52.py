# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. 
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. 
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

cant1=0
cant2=0
cant3=0
cant4=0

puntos=int(input("Cantidad de puntos: "))

for x in range(puntos):
    x=int(input("Ingrese coordenada x: "))
    y=int(input("Ingrese coordenada y: "))
    
    if x>0 and y>0:
        cant1=cant1+1
    else:
        if x<0 and y>0:
            cant2=cant2+1
        else:
            if x<0 and y<0:
                cant3=cant3+1
            else:
                if x>0 and y<0:
                    cant4=cant4+1

print(f"Cantidad de puntos en el primer cuadrante: {cant1}")
print(f"Cantidad de puntos en el segundo cuadrante: {cant2}")
print(f"Cantidad de puntos en el tercer cuadrante: {cant3}")
print(f"Cantidad de puntos en el cuarto cuadrante: {cant4}")