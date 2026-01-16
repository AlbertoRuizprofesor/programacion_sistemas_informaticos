#Ejercicio 136: Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios. Definir las siguientes funciones:
#1) Cargar los nombres de artículos y sus precios.
#2) Imprimir los nombres y precios.
#3) Imprimir el nombre de artículo con un precio mayor
#4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.

def cargar_articulos_precios():
    articulos=[]
    precios=[]
    for i in range(5):
        nombres1=input(f"Introduce un {i+1} nombre de un artículo: ")
        articulos.append(nombres1)
        precios1=int(input(f"Introduce el {i+1} precio: "))
        precios.append(precios1)
    return [articulos, precios]

def imprimir_nombres_precios(articulos,precios):
    print("Listado de articulos y precios")
    for i in range(len(articulos)):
        print(articulos[i], precios[i])
        
def imprimir_precio_mayor(articulos,precios):
    mayor=precios[0]
    contador=0
    for i in range(1,len(precios)):
        if precios[i]>mayor:
            mayor=precios[i]
            contador=i
    print("Articulo con un precio mayor es: ", articulos[contador], "por su precio es:",mayor)
    
def imprimir_precio_menor(articulos,precios):
    importe=int(input("Introduce un importe: "))
    for i in range(len(precios)):
        if precios[i]<=importe:
            print(articulos[i], precios[i])
            

articulos, precios=cargar_articulos_precios()
imprimir_nombres_precios(articulos,precios)
imprimir_precio_mayor(articulos,precios)
imprimir_precio_menor(articulos,precios)


            
            
    
    
    