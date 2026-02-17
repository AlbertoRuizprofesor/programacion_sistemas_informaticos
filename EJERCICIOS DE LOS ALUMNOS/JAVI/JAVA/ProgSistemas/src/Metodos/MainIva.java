package Metodos;

import java.util.Scanner;

public class MainIva {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		iva obj = new iva();
		
		System.out.println("Introduzca el importe: ");
		double num = teclado.nextDouble();
		
		obj.importe = num;
		
			
		obj.resultados();		
		
		
		teclado.close();
		

	}

}
