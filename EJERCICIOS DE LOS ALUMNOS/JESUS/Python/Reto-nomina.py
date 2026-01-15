# RETO 1: POO***********************************************************************************************
 
#  Realizar con programación en objeto una nomina, ejemplo, realizarlo con las funciones que sea necesario.
 
#  nombre: Alberto
#  Puesto: Docente
#  Nómina: 2400
#  IRPF: si los ingresos anuales son mayores de 30.000 21% y sin menores 15% de retención
 
#  Resultado:
 
# nombre: Alberto
# Puesto: Docente
# Nómina bruta: 2400
# Nómina anual bruta: 24.000
# Retención 15%: (la cantidad anual)
# Salario neto (anual bruto-retencion)
 
class Trabajador:

    def __init__(self):
        self.nombre=input("Pon el nombre: ")
        self.puesto=input("Ingresa el Puesto: ")
        self.nomina_bruto=int(input("ingresa el bruto de la nomina: "))
    
    def calc_bruto(self):
        self.bruto=self.nomina_bruto*14
        print(f"Nomina anual bruta: {self.bruto}")
        #return self.bruto
    
    def calc_retencion(self):
        retencion15=0.15
        retencion21=0.21
        
        #print(retencion)

        if self.bruto>=30000:
            #self.bruto*retencion21
           
            print(f"Retencion 21% {self.bruto*retencion21}")
            print(f"Neto bruto - retenciones {self.bruto-self.bruto*retencion21}")
        else:
            #self.bruto*retencion15
            print(f"Retencion 15% {self.bruto*retencion15}")
            print(f"Neto bruto - retenciones {self.bruto-self.bruto*retencion15}")
        
   
trabajador1=Trabajador()
trabajador1.calc_bruto()
trabajador1.calc_retencion()
