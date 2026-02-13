package metodos;

public class MainOperacionesEjemplo {
	public static void main (String[] args) {
		
		int numero1=10;
		int numero2=5;
		
	OperacionesEjemplo operaciones=new OperacionesEjemplo();
	int sumatorio=operaciones.sumar(numero1, numero2);
	operaciones.sumar(numero1,numero2);
	System.out.println("La suma es "+sumatorio);
	
	}

}
