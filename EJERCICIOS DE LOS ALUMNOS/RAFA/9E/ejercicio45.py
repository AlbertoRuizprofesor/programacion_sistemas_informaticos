mul3=0
mul5=0
nomul=0
mul3y5=0

for x in range(10):
    valor=int(input("ingrese valor"))
    if valor%3==0 and valor%5==0:
        mul3y5 += 1
    elif valor%5==0:
        mul5 += 1
    elif valor%3==0:
        mul3=mul3+1
    else:
        nomul=nomul+1 
print("multiplos de 3: ", mul3)
print("multipos de 5: ", mul5)
print("no multiplo de 3 ni de 5: ", nomul)
print("multiplo de 3 y de 5: ", mul3y5)

