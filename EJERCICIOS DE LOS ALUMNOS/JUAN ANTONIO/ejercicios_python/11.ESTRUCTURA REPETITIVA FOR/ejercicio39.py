#Realizar un programa que imprima en pantalla los números del 0 al 100. 
#Este problema lo podemos resolver perfectamente con el ciclo while pero en esta situación lo resolveremos empleando el for.

#Recorremos los números del 0 al 100
for x in range(101):
    print(x, end = " ") #Imprimimos cada número en la misma línea gracias a end = " "
                        #end = " " evita el salto de línea y añada un espacio después de cada número