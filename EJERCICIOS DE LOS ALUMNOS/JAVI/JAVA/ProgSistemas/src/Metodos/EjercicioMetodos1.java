package Metodos;

public class EjercicioMetodos1 {
	
	public static int sumar (int numero1, int numero2) {
		return numero1+numero2;
	}
	
	public static int restar (int numero1, int numero2) {
		return numero1-numero2;
	}
	
	public static int multiplicar (int numero1, int numero2) {
		return numero1*numero2;
	}
	
	public static int dividir (int numero1, int numero2) {
		if (numero1 > numero2) {
			return numero1/numero2;
		} else {
			return numero2/numero1;
		}
	}
	
	/*public static void saludar(String nombre) {
		System.out.println("Hola" + nombre);
	}
	*/

	public static void main(String[] args) {
		
		int numero1 = 24;
		int numero2 = 12;
		System.out.println("La suma es: " +(sumar(numero1, numero2)));
		System.out.println("La resta es: " +(restar(numero1, numero2)));
		System.out.println("La multiplicación es: " +(multiplicar(numero1, numero2)));
		System.out.println("La división es: " +(dividir(numero1, numero2)));

	}
	
}


