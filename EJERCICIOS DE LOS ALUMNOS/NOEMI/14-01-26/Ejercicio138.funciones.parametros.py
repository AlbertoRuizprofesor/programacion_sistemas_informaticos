#Ejercicio 138: Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter. La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro


def cadena_subrayada(titulo, caracter="*"):
    print(titulo)
    print(caracter*len(titulo))
    
    
    
cadena_subrayada("Sistema de Administracion.") 
cadena_subrayada("Ventas","-")