
producto=input("Nombre del producto (alimentacion/informatica/cursos):")
importe=int(input("Importe del producto:"))


if producto=="alimentacion":
    iva=importe*0.07
if producto=="informatica":
    iva=importe*0.21
if producto=="cursos":
    iva=importe*0
    
total=importe+iva
    
print("Su producto es", producto) 
print("Su importe es", importe) 
print("El iva es",iva )  
print("El total es", total)
    
    
    