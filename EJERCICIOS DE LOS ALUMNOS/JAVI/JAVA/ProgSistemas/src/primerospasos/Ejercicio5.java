package primerospasos;

import java.util.Scanner;

public class Ejercicio5 {

	public static void main(String[] args) {
		
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduzca el año de nacimiento: ");
		int nacimiento = teclado.nextInt();
		
		int actual = 2026;
		
		int edad = actual - nacimiento;		
		
		long meses = (long) edad * 12;
		long dias = (long) edad * 365;
		long horas = dias * 24;
		long minutos = horas * 60;
		long segundos = minutos * 60;				
		
		System.out.println("El año actual es: " + actual);
		System.out.println("Tu edad es: " + edad);
		System.out.println("En meses sería: " + meses + " meses.");
		System.out.println("En días sería: " + dias + " días.");
		System.out.println("En horas sería: " + horas + " horas.");
		System.out.println("En minutos sería: " + minutos + " minutos.");
		System.out.println("En segundos sería: " + segundos + " segundos.");	
		
		
		teclado.close();
	}

}

