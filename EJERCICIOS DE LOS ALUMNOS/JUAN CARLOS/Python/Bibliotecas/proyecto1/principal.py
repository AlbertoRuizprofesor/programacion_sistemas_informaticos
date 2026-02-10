
import operacioneslista
import mayormenor as mm
#Funciones
def mensaje(mensaje):
    print(f"\n=== === === {mensaje} === === ===")

lista=operacioneslista.cargar()
operacioneslista.imprimir_mayor(lista)
operacioneslista.imprimir_suma(lista)
operacioneslista.imprimir_resta(lista)
operacioneslista.imprimir_multiplicacion(lista)
mensaje("Usando Biblioteca MM")
print(f"El valor Mayor es: {mm.valorMayor(lista)}")
print(f"El valor Menor es: {mm.valorMenor(lista)}")


