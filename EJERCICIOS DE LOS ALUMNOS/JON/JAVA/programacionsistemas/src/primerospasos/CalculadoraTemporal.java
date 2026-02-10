package primerospasos;
import java.util.Scanner;

public class CalculadoraTemporal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub


		Scanner c=new Scanner(System.in);
		System.out.printf("Introduce tu año de nacimiento:  ");
		int anacim=c.nextInt();
		System.out.printf("Introduce el año actual:  ");
		int aact=c.nextInt();
		
		int edad,mes,dias,horas,minutos;
		
		edad=aact-anacim;
		mes=edad*12;
		dias=mes*31;
		horas=dias*24;
		minutos=horas*60;
		
		System.out.println("Tu edad es: " + edad);
		System.out.println("Has vivido todo este tiempo: ");
		System.out.println(+ edad +" Años");
		System.out.println(+ mes +" meses");
		System.out.println(+ dias +" Días");
		System.out.println(+ horas +" Horas");
		System.out.println(+ minutos +" Minutos");
	}

}
