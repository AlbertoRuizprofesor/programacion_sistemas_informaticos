package Bucles;

import java.util.Scanner;

public class Fibonacci {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s=new Scanner(System.in);
		System.out.printf("Introduce el número de elementos a mostrar: ");
		int num=s.nextInt();
		System.out.println("Secuencia de Fibonacci con For");
		int a=0,b=1;
		for (int i=1;i<=num;i++) {
			System.out.printf(a +", ");
			int sumafor=a+b;
			a=b;
			b=sumafor;
		}
		System.out.println("Fin");
		
		
		System.out.println("---------------------------------------------");
		System.out.println("Secuencia de Fibonacci con While");
		int i=0;
		int c=0,d=1;
		while (i<num) {
			System.out.printf(c +", ");
			int sumawhile=c+d;
			c=d;
			d=sumawhile;
			i++;
		}
		System.out.println("Fin");
		
		
		System.out.println("---------------------------------------------");
		System.out.println("Secuencia de Fibonacci con Do While");
		int j=0;
		int e=0,f=1;
		do {
			System.out.printf(e +", ");
			int sumadowhile=e+f;
			e=f;
			f=sumadowhile;
			j++;
		}while (j<num);
		System.out.println("Fin");
		System.out.println("---------------------------------------------");
	}

}
