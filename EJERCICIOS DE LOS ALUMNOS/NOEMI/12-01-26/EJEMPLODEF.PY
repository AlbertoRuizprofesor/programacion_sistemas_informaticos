#EJEMPLO DEF:

notas=[]
#añadir listas multidimensionales
 
n = int(input("¿Cuántas asignaturas quieres añadir? "))

for _ in range(n):
    asignatura = input("Nombre de la asignatura: ")
    notas = int(input("Nota: "))

    # Añadimos a la lista 2D
    notas.append([asignatura, notas])
    
 
numero1=float(input("Introduce el primer número: "))
numero2=float(input("Introduce el segundo número: "))

def sumar(numero1,numero2):
    resultado=numero1+numero2
    print(f"El resultado de la suma es: {resultado}")
    
def sumar2(numero1,numero2):
   resultado=numero1+numero2
   return resultado

sumar(numero1,numero2)
resultado_suma=sumar2(numero1,numero2)
print(f"la suma es: {resultado_suma}")