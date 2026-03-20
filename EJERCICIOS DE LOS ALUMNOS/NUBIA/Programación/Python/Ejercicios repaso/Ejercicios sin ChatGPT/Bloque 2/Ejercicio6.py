''' 
Implementa una agenda usando un diccionario donde la clave sea el nombre y el valor el teléfono. 
Crea un menú para añadir, buscar, modificar y borrar contactos. 
Idea clave: Haz que no se distingan mayúsculas y minúsculas en las búsquedas.
'''

agenda = {} 
 
while True: 
    print("AGENDA \n1. Añadir  \n2. Buscar  \n3. Modificar  \n4. Borrar  \n5. Listar  \n6. Salir") 
    opcion = input("Opción: ") 
 
    if opcion == "1": 
        nombre = input("Nombre: ").strip().lower() 
        telefono = input("Teléfono: ") 
        agenda[nombre] = telefono 
        
    elif opcion == "2": 
        nombre = input("Nombre a buscar: ").strip().lower() 
        print(agenda.get(nombre, "No encontrado")) 
        
    elif opcion == "3": 
        nombre = input("Nombre a modificar: ").strip().lower() 
        if nombre in agenda: 
            agenda[nombre] = input("Nuevo teléfono: ") 
        else: 
            print("No encontrado") 
            
    elif opcion == "4": 
        nombre = input("Nombre a borrar: ").strip().lower() 
        if nombre in agenda: 
            del agenda[nombre] 
        else: 
            print("No encontrado") 
            
    elif opcion == "5": 
        print("Contactos en la agenda:") 
        for nombre, telefono in agenda.items(): 
            print(f"· {nombre}: {telefono}") 
    elif opcion == "6": 
        break 
    
    else: 
        print("Opción no válida") 
