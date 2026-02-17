package Bucles;

import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduzca un número: ");
		
		int num = teclado.nextInt();		
		
	
		for(int i=1; i<=10;i++) {
			
			
			System.out.printf("%d x %d = %d%n", num, i, num * i);
		}
	
		System.out.println("****************");
		
		int contador = 0;
		while(contador < 10) {
			contador++;
		System.out.println(num + " x " + contador + " = " + (num*contador));
		}
		
		System.out.println("****************");
		
		int b =1;
		do {
			System.out.println(num + " x " + b + " = " + (num*b));
			b++;	
			
		} while (b <= 10);
		
		
		teclado.close();
	}

}
