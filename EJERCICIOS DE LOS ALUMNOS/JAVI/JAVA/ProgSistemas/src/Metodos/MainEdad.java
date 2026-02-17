package Metodos;

import java.util.Scanner;

public class MainEdad {

	public static void main(String[] args) {
		
		Edad obj = new Edad();
				
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduzca tu año de nacimiento: ");
		obj.nac = teclado.nextInt();		
				
		obj.resultados();

	}

}


