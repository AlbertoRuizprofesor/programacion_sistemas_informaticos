package Condicional;

//Lee importe y tipo (N normal, P premium, E empresa). Descuento: N=0%, P=10%, E=15%.

import java.util.Scanner;

public class Ejercicio10 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduce el importe: ");
			
		int importe = teclado.nextInt();
		
		System.out.print("Introduce el tipo: (N normal, P premium, E empresa) ");
		
		String tipo = teclado.next();
		
		if (tipo.equals("N")) {
			System.out.print("El precio es de: " + importe);
		} else if (tipo.equals("P")) {
			System.out.print("El precio es de: " + (importe - (importe * 0.10)));
		} else if (tipo.equals("E")) {
			System.out.print("El precio es de: " + (importe - (importe * 0.15)));
		} else {
			System.out.print("El tipo no es válido");
		}
		teclado.close();
	}

}
