"""
Se ingresan un conjunto de n alturas de personas por teclado. 
Mostrar la altura promedio de las personas.
"""

numero_alturas = int(input("¿Cuántas alturas quiere introducir?: "))
x = 0       # Contador para saber cuántas alturas llevamos
altura_total = 0    # Acumulador donde vamos sumando todas las alturas
promedio = 0        # Variable donde guardaremos el promedio
while x < numero_alturas:       # Repetimos tantas veces como alturas pidió el usuario
    altura = float(input("Introduzca una altura: "))    #Pedimos una altura
    altura_total = altura_total + altura    #La sumamos al total
    x += 1      #Avanzamos el contador
    promedio = altura_total / x     #Calculamos el promedio provisional

#Cuando el bucle termina, mostramos el promedio final con 2 decimales
print(f"La altura promedio de las personas es: {promedio:.2f}")

