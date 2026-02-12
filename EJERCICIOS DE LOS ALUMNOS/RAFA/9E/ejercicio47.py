
cantidad=0
n=int(input("Cuantos valores ingresará:"))


for x in range(n):
    base=int(input("base: "))
    altura=int(input("altura: "))
    superficie=base*altura
    print(("base: ",base),("altura: ",altura),("superficie: ", superficie))
    
    if superficie>12:
        cantidad=cantidad+1


print("cantidad superior a 12:", cantidad)
