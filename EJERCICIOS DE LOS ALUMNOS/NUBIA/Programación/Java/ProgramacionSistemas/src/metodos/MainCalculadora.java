package metodos;

public class MainCalculadora {

	public static void main(String[] args) {
		
	Calculadora callcal=new Calculadora();
	int suma = callcal.sumar(5, 3);
	int resta = callcal.restar(10, 5);
	int multip = callcal.multiplicar(3, 4);
	int divi = callcal.dividir(10, 2);
	
	System.out.println("La suma es "+suma);
	System.out.println("La resta es "+resta);
	System.out.println("La multiplicación es "+multip);
	System.out.println("La división es "+divi);

	}

}
