#De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
#a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
#c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.


#Ingreso de datos se almacenan en variables: sueldo y antiguedad
sueldo=int(input("Ingrese sueldo del empleado:"))
antiguedad=int(input("Ingrese su antiguedad en años:"))


# Primera condición: 
# # Si el sueldo es menor que 500 y la antigüedad es mayor a 10 años: aumento del 20%
if sueldo<500 and antiguedad>10:
    aumento=sueldo*0.20
    sueldototal=sueldo+aumento
    print("Sueldo a pagar")
    print(sueldototal)
else:   # Segunda condición: Si el sueldo es menor que 500 pero la antigüedad NO supera los 10 años: aumento del 5%
    if sueldo<500:
        aumento=sueldo*0.05
        sueldototal=sueldo+aumento
        print("Sueldo a pagar")
        print(sueldototal)
    else:   # Si el sueldo es 500 o más: no hay aumento
        print("Sueldo a pagar")
        print(sueldo)