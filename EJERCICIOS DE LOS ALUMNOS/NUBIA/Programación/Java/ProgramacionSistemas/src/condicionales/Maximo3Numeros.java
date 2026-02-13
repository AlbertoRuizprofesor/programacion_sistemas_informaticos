package condicionales;
import java.util.Scanner;

public class Maximo3Numeros {
	public static void main(String[] args) {
	
	Scanner c=new Scanner(System.in);
	
System.out.println("COMPARADOR DE NÚMEROS");
	
	System.out.print("Introduce el primer número: ");
	int numero1 = c.nextInt();
	
	System.out.print("Introduce el segundo número: ");
	int numero2 = c.nextInt();
	
	System.out.print("Introduce el tercer número: ");
	int numero3 = c.nextInt();
	
	if (numero1 == numero2 && numero2 == numero3) {
		System.out.print("Todos los números valen "+numero1);
	}
	else if (numero1 > numero2 && numero1 > numero3) {
		System.out.print(numero1+" es el mayor.");
	}
	else if (numero1 < numero2 && numero2 > numero3) {
		System.out.print(numero2+" es el mayor.");
	}
	else if (numero1 < numero2 && numero2 < numero3) {
		System.out.print(numero3+" es el mayor.");
	}
	
	c.close();
	
	}
}