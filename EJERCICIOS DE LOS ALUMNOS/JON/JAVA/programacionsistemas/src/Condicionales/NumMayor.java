package Condicionales;
import java.util.Scanner;

public class NumMayor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner a=new Scanner(System.in);
		System.out.println("Introduce el primer número:  ");
		int num1=a.nextInt();
		Scanner b=new Scanner(System.in);
		System.out.println("Introduce el segundo número:  ");
		int num2=b.nextInt();
		
		if(num1>num2) {
			System.out.println("El primer número es el mayor.");
		} else if (num1<num2) {
			System.out.println("El segundo número es el mayor.");
		} else {
			System.out.println("Los dos números son iguales.");
		}
		

	}

}
