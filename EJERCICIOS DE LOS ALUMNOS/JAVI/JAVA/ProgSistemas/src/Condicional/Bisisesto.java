package Condicional;

import java.util.Scanner;

//Un año es bisiesto si es divisible por 4 y no por 100, salvo que sea divisible por 400.

public class Bisisesto {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduce un número: ");
		
		int num = teclado.nextInt();
		
		if (num % 4 == 0 && num % 100 != 0 || num % 4 == 400){
			System.out.print(num + " es bisisesto");
		} else {
			System.out.print(num + " no es bisisesto");
		}
		
	}

}
