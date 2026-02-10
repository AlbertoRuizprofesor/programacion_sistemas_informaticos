#Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. 
#La carga de los valores hacerlo por teclado.

def mostrar(m1,m2,m3):
    if m1>m2 and m1>m3:
        print (m1)
    else:
        if m2>m3: 
            print(m2)
        else:
            print(m3)

def cargar():
    var1=int(input("ingrese el primer valor:"))
    var2=int(input("ingrese el segundo valor:"))
    var3=int(input("ingrese el tercer valor:"))    
    mostrar(var1,var2,var3)

#programa finalizado

cargar()