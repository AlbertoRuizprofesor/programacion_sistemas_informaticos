package Arrays;

import java.util.Scanner;

public class MainMetodo1 {

	public static void main(String[] args) {
		
		Metodo1 operacion = new Metodo1();
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduce el número1: ");
		
		int num1 = teclado.nextInt();
		
		System.out.println("Introduce el número2: ");
		
		int num2 = teclado.nextInt();
		
		int numero1 = num1;
		int numero2 = num2;		
		
		operacion.resultado(numero1, numero2);
		
		teclado.close();		
				
	}

}
