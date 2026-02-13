package condicionales;
import java.util.Scanner;

public class ParImpar {
	public static void main(String[] args) {
	Scanner c=new Scanner(System.in);
	
	System.out.print("Introduce un número entero: ");
	int entero1 = c.nextInt();
	
	if (entero1%2 == 0) {
		System.out.print("El número es par");
	}
	else {
		System.out.print("El número es impar");
	}
	
	c.close();
	}
}
