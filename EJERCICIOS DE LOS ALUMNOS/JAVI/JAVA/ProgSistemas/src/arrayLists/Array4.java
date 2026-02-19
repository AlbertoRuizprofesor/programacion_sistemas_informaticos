package arrayLists;

import java.util.ArrayList;

import java.util.Scanner;

public class Array4 {

	public static void main(String[] args) {

		ArrayList<String> nombres = new ArrayList<>();
		Scanner teclado = new Scanner(System.in);

		nombres.add("Alana");
		nombres.add("Bobby");
		nombres.add("Francisco");
		nombres.add("Rubén");
		nombres.add("Zaira");
		nombres.add("Beatriz");

		System.out.println("Introduzca el nombre: ");
		var buscar = teclado.nextLine();

		if (nombres.contains(buscar)) {
			System.out.print("El nombre está en la lista.");
		} else {
			System.out.print("El nombre NO está en la lista.");
		}
		
		teclado.close();

	}

}
