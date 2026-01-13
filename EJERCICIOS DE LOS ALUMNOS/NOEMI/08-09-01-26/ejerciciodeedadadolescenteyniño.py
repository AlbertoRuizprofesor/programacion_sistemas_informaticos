#Ejercicio:Edad e indica si es mayor o menor de edad.

nombre=input("Cuál es su nombre? ")
print("Buenos días,", nombre)

edad=int(input("Indique su edad: "))

if edad>=18 and edad<=65:
    print("Eres mayor de edad", nombre)
    
else:
    if edad>65:
        print("Jubilado")
        
    if edad>12 and edad<18:
        print("Es usted un adolescente insoportable")
        
    if edad<12:
        print("Es usted un niño feliz e insoportable")