package metodos;

public class Operaciones {
	
	
	public int sumar(int numero1, int numero2) {
		return numero1+numero2;	
	}
	
	public int restar(int numero1, int numero2) {
		return numero1-numero2;	
	}

	public int multiplicacion(int numero1, int numero2) {
		return numero1*numero2;	
	}

	public double division(int numero1, int numero2) {
		return numero1/numero2;	
	}
	
	public void lista_Operaciones(int numero1,int numero2 ) {
		int suma=sumar(numero1,numero2);
		int multi=multiplicacion(numero1,numero2);
		int resta=restar(numero1,numero2);
		double division=division(numero1,numero2);
		
		System.out.println("la suma es: "+suma);
		System.out.println("la resta es: "+resta);
		System.out.println("la multiplicacion es: "+multi);
		System.out.println("la division es: "+division);
		
		
	}
	
	
	

}
