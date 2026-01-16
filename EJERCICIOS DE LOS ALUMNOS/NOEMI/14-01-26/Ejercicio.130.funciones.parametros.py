#Ejercicio 130: Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja. En el bloque principal iniciamos por asignación la lista de string:


def contar_caracteres(lista):
    mas=0
    for i in range(len(lista)):
        if len(lista[i])>len(lista[mas]):
            mas=i
    return lista[mas]
    
    
    
lista=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
print("La palabra con mas caracteres:",contar_caracteres(lista))

