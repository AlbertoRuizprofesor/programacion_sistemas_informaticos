#Ejercicio 74: Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.

lista=["Noemi","ana","Nubia","jose","alberto"]

x=0
cantidad=0

while x<len(lista):
    if len(lista[x])>=5:
        cantidad+=1
    x=x+1
    
print("Todos los nombres de la lista son:", lista)
print("Los nombres que contienen 5 o más caracteres son: ", cantidad)