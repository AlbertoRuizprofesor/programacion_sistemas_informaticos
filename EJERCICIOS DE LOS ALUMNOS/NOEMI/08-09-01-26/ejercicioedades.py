#Ejercicio:Edad e indica si es mayor o menor de edad.

nombre=input("Cuál es su nombre? ")
print("Buenos días,", nombre)

edad=int(input("Indique su edad: "))

if edad<18:
    print("Eres menor de edad", nombre)
    
else:
    print("Eres mayor de edad", nombre)