#Escribe un programa en Python que pregunte al usuario qué animal le gusta más entre las siguientes opciones:
# 1. Perro
# 2. Gato
# 3. Pájaro
# 4. Otro

#Se imprime en consola las distintas opciones
print("Elige a tu animal favorito: ")
print("1. Perro")
print("2. Gato")
print("3. Pájaro")
print("4. Otro")

#El ususario introduce el número de su animal favorito
opcion = input("Escribe el número de tu animal favorito: ")

#Evaluación de los distintos casos y respuesta a cada caso
match opcion:
    case "1":
        print("Has elegido al Perro")
    case "2":
        print("Has elegido al Gato")
    case "3":
        print("Has elegido al Pájaro")
    case _:
        print("Has introducido un dato no válido")



