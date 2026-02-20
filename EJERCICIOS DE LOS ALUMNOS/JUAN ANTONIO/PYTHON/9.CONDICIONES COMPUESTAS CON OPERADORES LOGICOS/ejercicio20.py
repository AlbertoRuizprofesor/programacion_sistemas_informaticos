#Se carga una fecha (día, mes y año) por teclado. 
# Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo) 
# Cargar por teclado el valor numérico del día, mes y año.

# Pedimos al usuario que ingrese el número de día, el mes y el año
dia=int(input("Ingrese numeroro de día:"))
mes=int(input("Ingrese numero de mes:"))
año=int(input("Ingrese numero de año:"))


# Comprobamos si el mes ingresado pertenece al primer trimestre del año 
# El primer trimestre incluye los meses 1 (enero), 2 (febrero) y 3 (marzo)
if mes==1 or mes==2 or mes==3:
    print("Corresponde al primer trimestre")