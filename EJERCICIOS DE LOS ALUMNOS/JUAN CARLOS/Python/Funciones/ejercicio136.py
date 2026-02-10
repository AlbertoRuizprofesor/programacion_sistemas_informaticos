"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def entradaArticulos(numeroArticulos):
    listaNombres = []
    listaPrecios = []
    for cnt in range(numeroArticulos):
        nombre = input(f"Introduce el nombre del artículo {cnt + 1}: ")
        precio = float(input(f"Introduce el precio de {nombre}: "))
        listaNombres.append(nombre)
        listaPrecios.append(precio)
    return [listaNombres, listaPrecios]

def imprimirArticulos(nombres, precios):
    print("Artículos y precios:")
    for cnt in range(len(nombres)):
        print(f"{nombres[cnt]}: ${precios[cnt]}")

def articuloPrecioMayor(nombres, precios):
    mayor_precio = precios[0]
    art_mayor = nombres[0]
    for cnt in range(len(nombres)):
        if precios[cnt] > mayor_precio:
            mayor_precio = precios[cnt]
            art_mayor = nombres[cnt]
    return art_mayor

def mostrarMenorIgualImporte(nombres, precios):
    importe = float(input("Introduce el importe máximo: "))
    print(f"Artículos con precio <= ${importe}:")
    for cnt in range(len(precios)):
        if precios[cnt] <= importe:
            print(nombres[cnt])


#Main
listaNombres, listaPrecios = entradaArticulos(5)
mensaje("1. Carga completada")

mensaje("2. Todos los artículos")
imprimirArticulos(listaNombres, listaPrecios)

art_mayor = articuloPrecioMayor(listaNombres, listaPrecios)
mensaje("3. Artículo con precio mayor")
print(f"{art_mayor}")

mensaje("4. Filtrar por importe")
mostrarMenorIgualImporte(listaNombres, listaPrecios)

mensaje("Fin del programa")
