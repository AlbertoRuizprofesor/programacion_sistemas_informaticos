package primerospasos;

import java.util.Scanner;

public class Ejercicio6 {

	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("¿Cuánto tiempo dedicas al día al trabajo? ");
		int trabajo = teclado.nextInt();
		System.out.println("Trabajas " + trabajo * 5 + " horas semanales.");
		
		System.out.print("¿Cuánto tiempo dedicas al día a las tareas de la casa? ");
		int tareas = teclado.nextInt();
		System.out.println("Trabajas " + tareas * 7 + " horas semanales.");
		
		System.out.print("¿Cuánto tiempo dedicas al día al gym? ");
		int gym = teclado.nextInt();
		System.out.println("Entrenas " + gym * 4 + " horas semanales.");
		
		System.out.print("¿Cuánto tiempo dedicas a estudiar? ");
		int estudio = teclado.nextInt();
		System.out.println("Estudias " + estudio * 7 + " horas semanales.");
		
		System.out.print("¿Cuánto tiempo dedicas al día a pasear? ");
		int pasear = teclado.nextInt();
		System.out.println("Paseas " + pasear * 6 + " horas semanales.");
		
		System.out.print("¿Cuánto tiempo dedicas a leer? ");
		int leer = teclado.nextInt();
		System.out.println("Lees " + leer * 3 + " horas semanales.");
		
		
		teclado.close();
	}

}
