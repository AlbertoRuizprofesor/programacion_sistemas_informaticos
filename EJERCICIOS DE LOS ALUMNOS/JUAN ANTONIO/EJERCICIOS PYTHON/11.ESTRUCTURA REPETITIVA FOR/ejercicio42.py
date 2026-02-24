#Imprimir todos los números impares que hay entre 1 y 100.

# Recorremos los números desde el 1 hasta el 99 
# El tercer parámetro del range (2) indica que avanzamos de 2 en 2 
# Por eso solo se imprimen números impares

for x in range(1,100,2):
    print(x, end= " ")  #Imprimimos los números en la misma línea