# Ejercicio 196: Crear una agenda de contactos utilizando POO con las siguientes funcionalidades:


class Agenda:

    def __init__(self):
        self.contactos = {}  # definimos un diccionario para almacenar los datos

    def menu(self):
        opcion = 0
        while opcion != 5:
            print(
                "\n\033[36m1-\033[0m \033[32mCarga de un contacto en la agenda\033[0m"
            )
            print("\033[36m2-\033[0m \033[32mListado completo de la agenda\033[0m")
            print(
                "\033[36m3-\033[0m \033[32mConsulta ingresando el nombre de la persona\033[0m"
            )
            print("\033[36m4-\033[0m \033[32mModificacion del telefono y mail\033[0m")
            print("\033[36m5-\033[0m \033[31mFinalizar programa\033[0m\n")
            opcion = int(input("\033[33mIngrese su opcion:\033[0m "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listado()
            elif opcion == 3:
                self.consulta()
            elif opcion == 4:
                self.modificacion()

    def cargar(self):
        nombre = input("Ingrese el nombre de la persona:").lower()
        telefono = input("Ingrese el numero de telefono:")
        mail = input("Ingrese el mail:")
        self.contactos[nombre] = (telefono, mail)
        print("______________________________________________")

    def listado(self):
        print("______________________________________________")
        print("Listado completo de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0], self.contactos[nombre][1])
        print("______________________________________________")

    def consulta(self):
        print("______________________________________________")
        nombre = input("Ingrese el nombre de la persona a consultar:")
        if nombre in self.contactos:

            print(
                "\033[38m",
                nombre,
                " su telefono es",
                self.contactos[nombre][0],
                "y su mail es",
                self.contactos[nombre][1],
                "\033[0m",
            )
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")

    def modificacion(self):
        print("______________________________________________")
        nombre = input(
            "Ingrese el nombre de la persona a modificar el telefono y mail:"
        )
        if nombre in self.contactos:
            telefono = input("Ingrese el nuevo telefono:")
            mail = input("Ingrese el nuevo mail:")
            self.contactos[nombre] = (telefono, mail)
        else:
            print("No existe un contaxto con ese nombre")
        print("______________________________________________")


# bloque principal

agenda = Agenda()
agenda.menu()
