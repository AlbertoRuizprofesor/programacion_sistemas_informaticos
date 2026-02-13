package holamundo;
import java.util.Scanner;

public class Edad {

	public static void main(String[] args) {
		Scanner c=new Scanner(System.in);
		
		System.out.println("Ingresa tu año de nacimiento: ");
		int anual = c.nextInt();
		
		int actual=2026;
				
		int edad=actual-anual;
		
		System.out.println("Su edad es "+edad);
		
		c.close();
		
	}
	
}
