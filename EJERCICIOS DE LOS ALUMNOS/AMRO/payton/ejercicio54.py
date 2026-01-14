suma1=0
suma2=0
suma3=0
for f in range(5):
    edad=int(input("Ingrese edad:"))
    suma1=suma1+edad
media_edades1=suma1/5
print("La media de edades del turno mañana es ")
print(media_edades1)

for f in range(6):
    edad=int(input("Ingrese edad:"))
    suma2=suma2+edad
media_edades2=suma2/6
print("La media de edades del turno tarde es ")
print(media_edades2)

for f in range(11):
    edad=int(input("Ingrese edad:"))
    suma3=suma3+edad
media_edades3=suma3/11
print("La media de edades del turno noche es ")
print(media_edades3)

if media_edades1>media_edades2 and media_edades1>media_edades3:
    print("El turno mañana tiene el promedio de edades más alto.")    
else:
    if media_edades2>media_edades3:
        print("El turno tarde tiene el promedio de edades más alto.")
    else:
        print("El turno noche tiene el promedio de edades más alto.")              