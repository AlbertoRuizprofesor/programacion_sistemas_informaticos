"""
Confeccionar una clase que administre una agenda personal. 
Se debe almacenar el nombre de la persona, 
teléfono y mail Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

class Agenda:

    def __init__(self):
        self.contactos = {}

    def menu(self):
        opcion = 0
        while opcion != 5:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Modificacion del telefono y mail")
            print("5- Finalizar programa")

            opcion = int(input("Elige una opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.consultar()
            elif opcion == 4:
                self.editar()

    def cargar(self):        
        nombre = input("Introduce el nombre: ")
        telefono = int(input("Introduce su telefono: "))
        email = input("Introduce su email: ")
        self.contactos[nombre] = (telefono,email)
        print("_______________________________________")

    def listar(self):
        print("_______________________________________")
        print("Lista de la agenda: ")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0], self.contactos[nombre][1])
        print("_______________________________________")

    def consultar(self):
        print("______________________________________________")
        nombre=input("Ingrese el nombre de la persona a consultar:")
        if nombre in self.contactos:
            print(nombre,"su telefono es",self.contactos[nombre][0],"y su mail es",self.contactos[nombre][1])
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")

    
    def editar(self):
        print("______________________________________________")
        nombre=input("Ingrese el nombre de la persona a modificar el telefono y mail:")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo telefono:")
            mail=input("Ingrese el nuevo mail:")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un contaxto con ese nombre")
        print("______________________________________________")

       
            
agenda=Agenda()
agenda.menu()