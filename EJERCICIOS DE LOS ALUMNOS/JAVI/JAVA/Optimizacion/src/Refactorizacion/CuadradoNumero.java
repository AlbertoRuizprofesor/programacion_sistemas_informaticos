package Refactorizacion;

import java.util.Scanner;

//Definición de la clase principal del programa
public class CuadradoNumero {

	// Método principal que inicia la ejecución del programa
	public static void main(String[] args) {
		// Crear un objeto Scanner para leer la entrada del usuario
		Scanner scanner = new Scanner(System.in);

		// Solicitar al usuario que ingrese un número y calcular su cuadrado
		System.out.print("Ingrese un número: ");
		int numero = scanner.nextInt();

		// Utilizar código embebido para calcular el cuadrado del número
		int cuadrado = (int) Math.pow(numero, 2);

		// Mostrar el resultado al usuario
		System.out.println("El cuadrado del número es: " + cuadrado);

		// Cerrar el objeto Scanner
		scanner.close();
	}
}
