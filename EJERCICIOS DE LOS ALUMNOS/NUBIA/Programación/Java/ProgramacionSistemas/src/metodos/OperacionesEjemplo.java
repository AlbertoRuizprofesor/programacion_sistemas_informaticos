package metodos;

public class OperacionesEjemplo {
	
	// Método que devuelve un valor
	public int sumar(int numero1, int numero2) {
		return numero1+numero2;	
	}
	
	// Método con void
	public void restar(int numero1, int numero2) {
		System.out.println("La resta es "+(numero1-numero2));
	}

	public void operaciones(int numero1, int numero2) {
		int suma=sumar(numero1, numero2);
		System.out.println("La suma es "+suma);
		System.out.println("La resta es "+(numero1-numero2));
		
	}
}
