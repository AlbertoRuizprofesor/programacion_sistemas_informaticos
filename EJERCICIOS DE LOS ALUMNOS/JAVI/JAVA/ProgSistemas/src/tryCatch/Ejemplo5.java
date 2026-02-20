package tryCatch;

public class Ejemplo5 {

	public static void main(String[] args) {

		int a = 5;
		int b = 0;
		try {
			int resultado = Calculadora.dividir(a, b);
			System.out.println("Resultado: " + resultado);
		} catch (IllegalArgumentException e) {
			System.out.println("Error: " + e.getMessage());
		}
	}

}
