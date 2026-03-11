package Refactorizacion;

public class OperacionesMatematicas {

	public static int sumar(int num1, int num2) {
		return num1 + num2;
	}

	public static int restar(int num1, int num2) {
		return num1 - num2;
	}

	public static void mostrarResultado(int resultado) {
		System.out.println("El resultado es: " + resultado);
	}

	public static void main(String[] args) {
		int num1 = 10;
		int num2 = 5;

		int suma = sumar(num1, num2);
		int resta = restar(num1, num2);

		mostrarResultado(suma);
		mostrarResultado(resta);
	}
}
