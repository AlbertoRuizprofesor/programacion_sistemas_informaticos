package Condicionales;
import java.util.Scanner;

public class Edades {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c=new Scanner(System.in);
		System.out.println("Introduce tu edad: ");
		int edad=c.nextInt();
		
		if (edad<18) {
			System.out.print("Eres menor de edad.");

		} else if (edad>=18) {
			System.out.print("Eres mayor de edad.");
			
		}

	}

}
