package Condicional;

import java.util.Scanner;

public class SwitchCase {

	public static void main(String[] args) {

		Scanner teclado = new Scanner(System.in);

		System.out.print("Elige un número: ");
		int numero = teclado.nextInt();

		switch (numero) {

		case 1:
			System.out.print("has elegido 1");
			break;

		case 2:
			System.out.print("has elegido 2");
			break;

		case 3:
			System.out.print("has elegido 3");
			break;
		default:
			System.out.print("No has elegido.");

		}

		teclado.close();

	}

}
