# Pedimos que el usuario introduzca su edad
edad = int(input("Dime tu edad: "))

# Creamos la condicion 'if'
if edad>=18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Esta condición compara el valor de que ha dado el usuario con el número 18.
# El 'if' leido de manera humana dice: 'Si la edad introducida por el usuario es mayor o igual a 18, haz un print("....")...'.
# Ahora si no se cumple la condición del 'if' pasariamos al 'else' que leido de manera humana seria: '... si no, haz un print("...")'.
# Leido al completo sería: 'Si la edad es mayor o igual a 18, haz un print("...") si no, haz un print("..."")'. 