package Condicionales;
import java.util.Scanner;


public class MaximoDe3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner a=new Scanner(System.in);
		System.out.println("Introduce el primer número:  ");
		int num1=a.nextInt();
		Scanner b=new Scanner(System.in);
		System.out.println("Introduce el segundo número:  ");
		int num2=b.nextInt();
		Scanner c=new Scanner(System.in);
		System.out.println("Introduce el tercer número:  ");
		int num3=c.nextInt();
		
		if(num1>num2 && num1>num3) {
			System.out.println("El primer número es el mayor.");
		} else if (num2>num1 && num2>num3) {
			System.out.println("El segundo número es el mayor.");
		} else if (num3>num1 && num3>num2) {
			System.out.println("El tercer número es el mayor.");
		} else {
			System.out.println("Los tres números son iguales.");
		}

	}

}
