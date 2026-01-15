#En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
# 1) Carga de los sueldos en una lista.
# 2) Impresión de todos los sueldos.
# 3) Cuántos tienen un sueldo superior a $4000.
# 4) Retornar el promedio de los sueldos
# 5) Mostrar todos los sueldos que están por debajo del promedio.


def sueldos_de_una_lista():
    s=[]
    for x in range(10):
        var=int(input("ingresa el sueldo:"))
        s.append(var)
    return s

def impresion_sueldos(s):
    print("listados de sueldos")
    for x in range(len(s)):
        print(s[x])

def sueldo_superior_4000(s):
    cant=0
    for x in range(len(s)):
        if s [x]>4000:
            cant=cant+1
    print("los empleados con sueldos superiores a 4000" , cant)

def promedio(s):
    p=0
    for x in range(len(s)):
        p=p+s[x]
    promedio=p/10
    return promedio

def salarios_bajos(s):
    k=promedio(s)
    print("el promedio del salario de la empresa es:" , k)
    print("los salarios inferiores al promedio son" )
    for x in range(len(s)):
            print(s[x])

#finalización:
s=sueldos_de_una_lista()
impresion_sueldos(s)
sueldo_superior_4000(s)
salarios_bajos(s)
