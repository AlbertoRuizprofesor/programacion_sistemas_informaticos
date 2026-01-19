# Listas y tuplas anidadas
# En general podemos crear y combinar tuplas con elementos de tipo lista y viceversa, es decir listas con componente tipo tupla.

empleado = ["Ana", 28, (5,3,1997)] 

empleado.append((18,1,2026))
print(empleado)

alumno = ("Pedro", [7,9]) 
print(alumno)

alumno[1].append(10) 
print(alumno)