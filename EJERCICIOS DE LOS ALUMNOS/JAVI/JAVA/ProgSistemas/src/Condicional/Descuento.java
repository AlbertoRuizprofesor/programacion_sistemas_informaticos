package Condicional;

import java.util.Scanner;

public class Descuento {

	public static void main(String[] args) {
		
		System.out.print("Introduce el importe: ");
		
		Scanner teclado = new Scanner(System.in);
		
		double importe = teclado.nextInt();
		
		if (importe > 0 && importe < 100) {
			
			System.out.print("El precio es de: " + importe);
			
		} else if (importe > 100 && importe < 1000) {
			double descuento = 0.10;
			System.out.print("El precio es de:  " + (importe  - (importe * descuento)));
			
		} else if (importe > 1000) {
			double descuento = 0.20;
			System.out.print("El precio es de:  " + (importe - (importe * descuento)));
	
		} else {
			System.out.print("No se puede introducir valores negativos. ");			
			
		}
		teclado.close();

	}

}
