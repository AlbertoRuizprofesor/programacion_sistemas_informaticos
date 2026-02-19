
package Metodos;

import java.util.Scanner;

public class Operaciones {

	public int sumar(int numero1, int numero2) {
		return numero1 + numero2;
	}

	public int restar(int numero1, int numero2) {
		return numero1 - numero2;
	}

	public int multiplicacion(int numero1, int numero2) {
		return numero1 * numero2;
	}

	public double division(int numero1, int numero2) {
		return numero1 / numero2;
	}
	
	public int multiplo(int numero1, int numero2, int numero3, int numero4) {
		return numero1 * numero2 * numero2 * numero1;
	}

	public void lista_Operaciones(int numero1, int numero2) {
		double[] operacion = new double[5];
		String[] nombre_opera = { "Suma", "Resta", "Multiplicación", "División", "Multiplo" };
		double [] op = {sumar(numero1, numero2), restar(numero1, numero2), multiplicacion(numero1, numero2),
		division(numero1, numero2), multiplo(numero1, numero2, numero2, numero2)};

		int i = 0;
		for (double numer : op) {

			System.out.println(" La " + nombre_opera[i] + " es: " + numer);
			i++;
		}

	}

	public int[] pedirDatos() {
		Scanner c = new Scanner(System.in);
		int[] numero = new int[2];

		for (int i = 0; i < numero.length; i++) {
			System.out.print("Dime el numero " + (i + 1) + " : ");
			numero[i] = c.nextInt();
		}

		c.close();
		return numero;

	}

}



