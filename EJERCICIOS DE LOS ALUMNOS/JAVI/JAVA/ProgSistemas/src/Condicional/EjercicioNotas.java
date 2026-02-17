package Condicional;

import java.util.Scanner;

public class EjercicioNotas {

	public static void main(String[] args) {
		
		System.out.print("Introduce la nota: ");
		
		Scanner teclado = new Scanner(System.in);
		
		int nota = teclado.nextInt();
		
		if (nota < 5) {
			System.out.print("Estás suspenso ");
		} else if (nota < 6) {
			System.out.print("Tienes un 5 ");
		} else if (nota < 7) {
			System.out.print("Tienes un 6 ");
		} else if (nota < 8) {
			System.out.print("Tienes un 7 ");
		} else if (nota < 9) {
			System.out.print("Tienes un 8 ");
		} else if (nota < 10) {
			System.out.print("Tienes un 9 ");
		} else {
			System.out.print("Tienes un 10 ");
			
		}

	}

}
