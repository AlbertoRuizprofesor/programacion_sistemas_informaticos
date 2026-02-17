package Condicional;

// Lee un número e indica si está en el rango [10,20].
import java.util.Scanner;


public class Ejercicio13 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		System.out.print("Introduce un número: ");
		int num = teclado.nextInt();
		
		if (num >= 10 && num <= 20) {
			System.out.print(num + " está en el rango [10,20].");
		} else {
			System.out.print(num + " está en el rango [10,20].");
		}
		
	}

}
