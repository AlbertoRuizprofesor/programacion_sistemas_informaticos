a = 0
b = 1
c = 0
for i in range(12):
    a = b
    b = c
    c = a + b
    print(b)
