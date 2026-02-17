package Condicional;

import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduce un número: ");
		
		int num = teclado.nextInt();
		
		if (num % 2 == 0) {
			System.out.print( num + " es par.");
		} else {
			System.out.print( num + " es impar.");
		}
		
		teclado.close();

	}

}
