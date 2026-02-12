#Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".


#Pide al ususario que escriba un correo
mail=input("Ingrese un mail:")

#Inicializa variables
cantidad=0
x=0

#Recorre el correo dede la posición 0 hasta la última letra
#Comprueba cada caracter del correo contando las arrobas
while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1

#Si contiene una arroba es correcto, si hay cero o más de 1 es incorrecto
if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")