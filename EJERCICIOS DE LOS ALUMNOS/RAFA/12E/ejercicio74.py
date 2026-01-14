lista=["carmen","laly","rafa","diana","minerva"]
contador=0
x=0

while x<len(lista):
    if len(lista[x])>=5:
        contador +=1
    x=x+1

print("elementos: ",lista)
print("mayor de 5: ",contador)