package Condicional;

import java.util.Scanner;

//Lee lados a,b,c. Comprueba si puede existir (cada lado < suma de los otros dos). 
//Si existe, indica: equilátero, isósceles o escaleno.

public class Ejercicio11 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduce el lado a: ");
		int a = teclado.nextInt();
		
		System.out.print("Introduce el lado b: ");
		int b = teclado.nextInt();
		
		System.out.print("Introduce el lado c: ");
		int c = teclado.nextInt();
		
		
		if (a == b && a == c) {
			System.out.print("El triángulo es equilátero.");
		} else if (a == b || a == c || b == c) {
				System.out.print("El triángulo es isósceles.");
		} else {
			System.out.print("El triángulo es escaleno.");
		}		
			

	}

}
