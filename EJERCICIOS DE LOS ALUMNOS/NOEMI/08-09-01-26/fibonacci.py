#fibonacci=[0,1]

#for i in range(10):
   # fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
#print(fibonacci)

a=0
b=1
c=0
print(a)
for x in range(11):
    a=b
    b=c
    c=a+b
    print(c)