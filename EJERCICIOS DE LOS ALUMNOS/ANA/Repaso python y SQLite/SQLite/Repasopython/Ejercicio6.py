#Implementa una agenda usando un diccionario donde la clave sea el nombre y el valor el teléfono. 
#Crea un menú para añadir, buscar, modificar y borrar contactos.
#Idea clave: Haz que no se distingan mayúsculas y minúsculas en las búsquedas.

agenda = {}

while True:
    print("1. Añadir 2.Buscar 3.Modificar 4.Borrar 5.salir")
    opcion = input("Opcion: ")

    if opcion == "1":
        nombre  = input ("Nombre: "). strip().lower()
        telefono = input ("Telefono: " )
        agenda[nombre] = telefono
    
    elif opcion == "2":
        nombre = input ("Nombre a buscar: ").strip().lower()

    elif opcion == 2:
        nombre = input("nombre a buscar: ").strip().lower()
        print(agenda.get(nombre, "no encontrado"))
    
    elif opcion == "4":
        nombre = input ("nombre a borrar: ").strip().lower()
        if nombre in agenda:
            del agenda [nombre]
        
        else:
            print("no encontrado")
    elif opcion == "4":
        break
    else:print("opcion no valida")
