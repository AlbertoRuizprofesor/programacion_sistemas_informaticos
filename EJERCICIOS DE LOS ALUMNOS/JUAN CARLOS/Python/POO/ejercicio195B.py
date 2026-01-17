"""
Confeccionar una clase que administre una agenda personal.
Se debe almacenar el nombre de la persona, teléfono y mail.
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

class Agenda:
    def __init__(self):
        self.contactos = []  # Lista de dicts: [{"nombre": "", "tel": "", "mail": ""}]

    def menu(self):
        print("\n=== AGENDA PERSONAL ===")
        print("1- Carga contacto")
        print("2- Listado completo")
        print("3- Consulta por nombre")
        print("4- Modificar tel/mail")
        print("5- Finalizar")
        return int(input("Opción: "))

    def cargar_contacto(self):
        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        mail = input("Mail: ").strip()
        self.contactos.append({"nombre": nombre, "tel": telefono, "mail": mail})
        print("Contacto cargado!")

    def listar_completo(self):
        if not self.contactos:
            print("Agenda vacía")
            return
        print("\nLISTADO COMPLETO:")
        for cnt in self.contactos:
            print(f"{cnt['nombre']} - {cnt['tel']} - {cnt['mail']}")

    def consultar_nombre(self):
        nombre_buscar = input("Nombre a consultar: ").strip().lower()
        for cnt in self.contactos:
            if cnt['nombre'].lower() == nombre_buscar:
                print(f"Nombre: {cnt['nombre']}")
                print(f"Tel: {cnt['tel']}, Mail: {cnt['mail']}")
                return
        print("Contacto no encontrado")

    def modificar_contacto(self):
        nombre_buscar = input("Nombre a modificar: ").strip().lower()
        for cnt in self.contactos:
            if cnt['nombre'].lower() == nombre_buscar:
                cnt['tel'] = input("Nuevo teléfono: ").strip()
                cnt['mail'] = input("Nuevo mail: ").strip()
                print("Modificado!")
                return
        print("Contacto no encontrado")


#Main
agenda = Agenda()
while True:
    opcion = agenda.menu()
    if opcion == 1:
        agenda.cargar_contacto()
    elif opcion == 2:
        agenda.listar_completo()
    elif opcion == 3:
        agenda.consultar_nombre()
    elif opcion == 4:
        agenda.modificar_contacto()
    elif opcion == 5:
        mensaje("Fin del programa")
        break
