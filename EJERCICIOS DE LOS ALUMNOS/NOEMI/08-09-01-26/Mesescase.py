#Ejercicio case con Meses.

mes=int(input("Introduce el numero del mes (1-12): "))

match mes:
    case 12 | 1 | 2:
        print("Es invierno")
    case 3 | 4 | 5:
        print("Es primavera")
    case 6 | 7 | 8 :
        print("Es verano")
    case 9| 10 | 11:
        print("Es otoño")
        
    
