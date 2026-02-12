""""
Confeccionar una clase que administre una agenda personal. 
Se debe almacenar el nombre de la persona, teléfono y mail 
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

class Agenda:

    def __init__(self):
        self.contactos={} # definimos un diccionario para almacenar los datos

    def menu(self):
        opcion=0
        while opcion!=5:
            print("1- Añadir contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Modificación del teléfono y mail")
            print("5- Finalizar programa")
            opcion=int(input("Ingrese su opción: "))
            print("-"*50)
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificacion()

    def cargar(self):
        nombre=input("Ingrese el nombre de la persona: ")
        telefono=input("Ingrese el número de teléfono: ")
        mail=input("Ingrese el mail: ")
        self.contactos[nombre]=(telefono,mail)
        print("-"*50)

    def listado(self):
        print("-"*50)
        print("Listado completo de la agenda:")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0],self.contactos[nombre][1])
        print("-"*50)

    def consulta(self):
        nombre=input("Ingrese el nombre de la persona a consultar: ")
        if nombre in self.contactos:
            print(f"El tlf de {nombre} es {self.contactos[nombre][0]} y su mail es {self.contactos[nombre][1]}")
        else:
            print("No existe un contacto con ese nombre")
        print("-"*50)

    def modificacion(self):
        nombre=input("Ingrese el nombre de la persona a modificar tlf y mail: ")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo teléfono: ")
            mail=input("Ingrese el nuevo mail: ")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un contaxto con ese nombre")
        print("-"*50)


# bloque principal

agenda=Agenda()
agenda.menu()





