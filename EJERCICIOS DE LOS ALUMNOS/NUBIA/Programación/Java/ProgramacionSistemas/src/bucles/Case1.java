package bucles;
import java.util.Scanner;

public class Case1 {
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		
		System.out.print("Elige un número entre 1 y 3: ");
		int numero = sc.nextInt();
		
		switch (numero) {
			case 1:
			System.out.println("Has elegido 1");
			break;
		
			case 2:
				System.out.println("Has elegido 2");
				break;
			
			case 3:
				System.out.println("Has elegido 3");
				break;
		}
		sc.close();
	}
	 
}
