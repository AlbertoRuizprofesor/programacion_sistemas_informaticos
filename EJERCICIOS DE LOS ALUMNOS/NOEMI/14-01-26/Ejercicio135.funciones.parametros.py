#Ejercicio 135: - En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
#1) Carga de los sueldos en una lista.
#2) Impresión de todos los sueldos.
#3) Cuántos tienen un sueldo superior a $4000.
#4) Retornar el promedio de los sueldos
#5) Mostrar todos los sueldos que están por debajo del promedio.


def carga_sueldos():
    lista=[]
    for i in range(10):
        sueldos=int(input(f"Introduce el {i+1} sueldo: "))
        lista.append(sueldos)
    return lista


def imprimir_sueldos(lista):
    print("Listado de sueldos.")
    for i in range(len(lista)):
        print(lista[i])
        

def sueldo_superior(lista):
    cant=0
    for i in range(len(lista)):
        if cant[i]>4000:
            cant=cant+1
    print("Cantidad de empleados con un sueldo superior a 4000: ", cant)
    
def promedio(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    promedio=suma//10
    return promedio

def sueldos_bajos(lista):
    pro=promedio(lista)
    print("Sueldo promedio de la empresa:", pro)
    print("Sueldos inferiores al promedio")
    for i in range(len(lista)):
        if lista[i]<pro:
            print(lista[i])  
            
lista=carga_sueldos
imprimir_sueldos(lista)
sueldo_superior(lista)
promedio(lista)
sueldos_bajos(lista)