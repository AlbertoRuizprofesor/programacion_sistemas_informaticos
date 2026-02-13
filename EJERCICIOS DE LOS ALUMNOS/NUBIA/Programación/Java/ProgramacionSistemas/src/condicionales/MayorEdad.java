package condicionales;
import java.util.Scanner;

public class MayorEdad {
	public static void main(String[] args) {
	Scanner c=new Scanner(System.in);
	
	System.out.print("Introduce tu edad: ");
	int edad= c.nextInt();
	
	if (edad<18) {
		System.out.print("Eres menor de edad.");
	}
	else if (edad>=18) {
		System.out.print("Eres mayor de edad.");
	}
c.close();
	}
}
