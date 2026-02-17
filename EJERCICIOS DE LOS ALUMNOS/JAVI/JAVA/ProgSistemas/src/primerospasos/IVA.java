package primerospasos;

import java.util.Scanner;


public class IVA {

	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduzca el importe: ");
		
		double num = teclado.nextDouble();
		
		System.out.print("Introduzca las unidades: ");
		
		int unidades = teclado.nextInt();
		
		double descuento = (num * unidades) * 0.10;
		
		double iva = 0.21;
		
		double total = (unidades * num - descuento);
		
		System.out.println("¡Hay descuento del 10%! " + descuento);
		
		System.out.println("El total es : " + total);
				
		System.out.println("El IVA (total) es : " +  (total * iva));
		
		System.out.println("El total a pagar es : " + (total + total * iva));
		
		teclado.close();

	}

}

