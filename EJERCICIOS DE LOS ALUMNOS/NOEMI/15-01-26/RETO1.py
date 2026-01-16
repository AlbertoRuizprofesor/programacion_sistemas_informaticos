#RETO 1:Realizar con programación en objeto una nomina, ejemplo, realizarlo con las funciones que sea necesario.
"""nombre: Alberto
Puesto: Docente
Nómina: 2400
IRPF: si los ingresos anuales son mayores de 30.000 21% y sin menores 15% de retención
 
Resultado:
 
nombre: Alberto
Puesto: Docente
Nómina bruta: 2400
Nómina anual bruta: 24.000
Retención 15%: (la cantidad anual)
Salario neto (anual bruto-retencion)"""

#HACER UN CONSTRUCTOR Y UNA/DOS FUNCION.
class Nomina:
    def __init__(self, nom="", puesto="",nomina=""):
        self.nom=nom
        self.puesto=puesto
        self.nomina=nomina
        
    def operaciones(self):
        
        anualbruta=self.nomina*10
         
        if anualbruta>30000:
            porcentaje=0.21
        else:
            porcentaje=0.15
            
       
        retencion=anualbruta*porcentaje
        salarioneto=anualbruta-retencion
        
        
        print("Nombre:",self.nom)
        print("Puesto:",self.puesto)       
        print("Nomina bruta:",self.nomina) 
        print("Nomina anual bruta:",anualbruta)
        print("Retención del IRPF:",retencion)
        print("Salario neto anual:",salarioneto)
       

nomina1=Nomina("Alberto","Docente",2400)
nomina1.operaciones()
        
        
                    