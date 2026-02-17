package Metodos;

import java.util.Scanner;

public class ainNotasMetodo {

	public static void main(String[] args) {

		NotasMetodo nota = new NotasMetodo();
		Scanner teclado = new Scanner(System.in);

		System.out.println("Introduzca la nota: ");
		int notalumno = teclado.nextInt();

		nota.num = notalumno;

		nota.mostrarNota();

		teclado.close();

	}

}
