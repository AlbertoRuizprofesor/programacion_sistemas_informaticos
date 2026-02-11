#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 
#En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ordenar (var1,var2,var3):
    if var1<var2 and var1<var3:
        if var2<var3:
            print(var1,var2,var3)
        else:
            print(var1,var3,var2)
    else:
        if var2<var3:
            if var1<var3:
                print(var2,var1,var3)
            else:
                print(var2,var3,var1)
        else:
            if var1<var2:
                print(var3,var1,var2)
            else:
                print(var3,var2,var1)
def cargar():
    var1=int(input("ingrsa el primer valor:"))
    var2=int(input("ingresa el segundo valor:"))
    var3=int(input("ingresa el tercer valor:"))
    ordenar(var1,var2,var3)

#pilar principal 
cargar()