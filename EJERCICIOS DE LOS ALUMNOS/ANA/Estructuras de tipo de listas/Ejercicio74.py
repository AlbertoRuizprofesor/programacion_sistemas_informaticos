#Definir una lista que almacene por asignación los nombres de 5 personas. 
#Contar cuantos de esos nombres tienen 5 o más caracteres.

lista=["Raúl", "Xavi", "Álvaro", "Verónica", "Sergio"]

#contar cuantos nombres tienen 5 o más caracteres

contador=0
for nombres in  lista:

    if len (nombres)>= 5:
        contador += 1

print("contador de 5 o más caracteres son" , contador)
