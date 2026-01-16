class Nomina:
    def __init__(self):
        self.nombre = input("Dame el nombre de la persona: ")
        self.puesto = input("Dime el puesto: ")
        self.nomina = float(input("Dime lo que gana: "))
        self.impresion()

    def nomina_anual_bruta(self):
        nomina_anual = self.nomina * 12
        return nomina_anual

    def retencion(self):
        anual = self.nomina_anual_bruta()
        if anual > 3000:
            porcenteaje = 21
        else:
            porcenteaje = 15
        cantidad = anual * (porcenteaje / 100)
        return cantidad, porcenteaje

    def salario_neto(self):
        nomina = self.nomina_anual_bruta()
        cantidad,porcentaje = self.retencion()
        sal_net = nomina - cantidad
        return sal_net
    
    def impresion(self):
        cantidad_retencion, porcentaje = self.retencion()
        print(f"\n------INFORMACION------\nNombre: {self.nombre}\nPuesto: {self.puesto}\nNómina: {self.nomina}\nNómina anual bruta: {self.nomina_anual_bruta()}\nRetención {porcentaje}%: {cantidad_retencion}\nSalario neto: {self.salario_neto()}")