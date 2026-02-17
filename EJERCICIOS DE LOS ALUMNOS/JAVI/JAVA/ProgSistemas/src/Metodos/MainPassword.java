package Metodos;

import java.util.Scanner;

public class MainPassword {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
				
		Password datos = new Password();
		
		System.out.println("Introduce usuario:");
		datos.user = teclado.nextLine(); 

		System.out.println("Introduce password:");
		datos.password = teclado.nextLine();
				
	
		datos.mostrar();
				
		
		
		teclado.close();

	}

}
