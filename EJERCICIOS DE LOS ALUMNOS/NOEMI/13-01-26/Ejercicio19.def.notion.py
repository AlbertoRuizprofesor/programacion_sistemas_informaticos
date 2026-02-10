#Ejercicio 119: Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.


def ordenar_imprimir(v1,v2,v3):
    if v1<v2 and v1<v3:
        if (v2<v3):
            print(v1,v2,v3)
        else:
            print(v1,v3,v2)
    else:
        if (v2<v3):
            if (v1<v3):
                print("v2,v1,v3")
            else:
                print("v2,v3,v1")
        else:
            if (v1<v2):
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)    
def cargar():
    n1=int(input("Introduce el primer valor: "))
    n2=int(input("Introduce el segundo valor: "))
    n3=int(input("Introduce el tercer valor: "))
    ordenar_imprimir(n1,n2,n3)
    
cargar()
    