# EJERCICIO RETO 1 SOLUCION, Y RETO 2 Y 3 SE HACEN IGUAL: solución
 
class Nomina:

    def __init__(self, nombre="",puesto="", nomina=0):
        self.nombre = nombre
        self.puesto = puesto
        self.nomina = nomina

    def calculo_irpf(self):
        print(f"Nombre: {self.nombre} Puesto: {self.puesto} Nomina: {self.nomina}")
        if (self.nomina)*12 > 24000:
            irpf = 0.21
        else:
            irpf = 0.15
        print(f"El IRPF es de: {irpf*100}%")
        print(f"El total a pagar de IRPF es: {(self.nomina*12)*irpf} euros anuales")    
        print(f"El salario neto mensual es: {self.nomina - ((self.nomina*12)*irpf)/12} euros mensuales")
        print(f"El salario neto anual es: {(self.nomina*12) - (self.nomina*12)*irpf} euros anuales")


# bloque principal
persona1 = Nomina("Pedro", "Desarrollador", 2400)
persona1.calculo_irpf()
 