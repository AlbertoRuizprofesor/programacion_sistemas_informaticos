package Condicional;

//Usuario correcto: admin, clave: 1234. Lee ambos y valida.

import java.util.Scanner;


public class Ejercicio12 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduce el usuario: ");
		
		String usuario = teclado.next();
		
		System.out.print("Introduce la clave: ");
		
		String clave = teclado.nextLine();
		
		if (usuario.equals("admin") && clave.equals("1234")) {
		      System.out.println("Acceso concedido");
		    } else {
		      System.out.println("Acceso denegado");
		    }
		    teclado.close();
		  }
		
	}


