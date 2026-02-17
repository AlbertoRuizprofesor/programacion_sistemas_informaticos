package Bucles;

import java.util.Scanner;

public class fibonacci {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		System.out.print("Introduzca el límite de la sucesión: ");
		int num = teclado.nextInt();
		
		int a = 0;
		int b = 1;
		
		for(int i=1; i <= num; i++) {
			
			System.out.println(a); 
			
			int c = a + b;
			a = b;
			b = c;
			
		}
			
		/*
		System.out.println("*************");
		
		int contador = 0;
		
		while(contador < num - 2) {
						
			int c = a + b;			
			a = b;
			b = c;
			
			System.out.println(c); 
			
			contador++;
			
		}
		*/
		
		teclado.close();
	}
	
}
