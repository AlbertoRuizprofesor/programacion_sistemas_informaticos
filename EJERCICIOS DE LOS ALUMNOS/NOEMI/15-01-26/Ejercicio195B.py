#Ejercicio 195B: Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail Debe mostrar un menú con las siguientes opciones:
#1- Carga de un contacto en la agenda.
#2- Listado completo de la agenda.
#3- Consulta ingresando el nombre de la persona.
#4- Modificación de su teléfono y mail.
#5- Finalizar programa.

class Agenda:
    
    def __init__(self):
        self.contactos={} #Diccionario para almacenar datos.
        
    def menu(self):
        opcion=0
        while opcion!=5:
            print("1-Carga de un contacto en la agenda.")
            print("2-Listado completo de la agenda.")
            print("3-Consulta ingresando el nombre de la persona.")
            print("4-Modificación de su teléfono y mail.")
            print("5- Finalizar programa.")
            
            opcion=int(input("Ingrese una opcion: "))
            
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificacion()
    
    def cargar(self):
        nombre=input("Ingrese el nombre de la persona:")
        telefono=input("Ingrese el numero de telefono:")
        mail=input("Ingrese el mail:")
        self.contactos[nombre]=(telefono,mail)    #Los corchetes son la sintaxis para deicr que nombre es la clave, y los parentesis son una tupla que es inmutable y es el valor de la clave.  
        print("______________________________________________")
        
    def listado(self):
        print("______________________________________________")
        print("Listado completo de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0],self.contactos[nombre][1])
        print("______________________________________________")
        
    def consulta(self):
        print("______________________________________________")
        nombre=input("Ingrese el nombre de la persona a consultar:")
        if nombre in self.contactos:
            print(nombre," su telefono es",self.contactos[nombre][0],"y su mail es",self.contactos[nombre][1])
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")
        
    def modificacion(self):
        print("______________________________________________")
        nombre=input("Ingrese el nombre de la persona a modificar el telefono y mail:")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo telefono:")
            mail=input("Ingrese el nuevo mail:")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")
        
agenda=Agenda()
agenda.menu()

        
        
        
    

        