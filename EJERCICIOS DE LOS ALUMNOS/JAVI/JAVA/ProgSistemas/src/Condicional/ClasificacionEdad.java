package Condicional;

import java.util.Scanner;

public class ClasificacionEdad {

	public static void main(String[] args) {
		
		System.out.print("Introduce la edad: ");
		
		Scanner teclado = new Scanner(System.in);
		
		int edad = teclado.nextInt();
		
		if (edad < 18) {
			System.out.print("Eres menor de edad ");
		} else if (edad < 30) {
			System.out.print("Eres joven ");
		} else if (edad < 40) {
			System.out.print("Eres treinteañero ");
		} else if (edad < 50) {
			System.out.print("Eres cuarentón ");
		} else if (edad < 60) {
			System.out.print("Eres cincuentón ");
		} else if (edad < 70) {
			System.out.print("Eres viejito ");
		} else {
			System.out.print("Estás pal arrastre ");
			
		}

	}

}
