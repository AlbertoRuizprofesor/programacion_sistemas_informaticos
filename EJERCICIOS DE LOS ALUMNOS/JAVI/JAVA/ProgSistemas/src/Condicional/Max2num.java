package Condicional;

import java.util.Scanner;

public class Max2num {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduce un número: ");
		int num1 = teclado.nextInt();
		System.out.print("Introduce un número: ");
		int num2 = teclado.nextInt();
		
		if (num1 > num2) {
			System.out.print(num1 + " es el mayor.");
		} else if (num1 < num2) {
			System.out.print(num2 + " es el mayor.");
		} else {
			System.out.print("Ambos números son iguales.");
			
		}

	}

}
