#Ejercicio piedra_papel_tijeras

import random
numero=random.randint(1, 3) 
if numero==1:
    print("usted ha elegido el papel")
else:
    if numero==2:
        print("la maquina ha elegido piedra")
    if numero==3:
        print("papel ganan a la piedra, Usted ha ganado")
        

