package Condicional;

import java.util.Scanner;

public class PositivoNegativo0 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduce un número: ");
		
		int num = teclado.nextInt();
		
		if (num == 0) {
			System.out.print(num + " es cero.");
		} else if (num > 0) {
			System.out.print(num + " es mayor que cero.");
		} else {
			System.out.print(num + " es menor que cero.");
		}
			
		
		teclado.close();

	}

}
