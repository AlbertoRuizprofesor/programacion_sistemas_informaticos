package primerospasos;
import java.util.Scanner;


public class Edad {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c=new Scanner(System.in);
		System.out.print("Dime tu año de nacimiento:");
		int anual=c.nextInt();
		int actual=2026;
		
		int edad=actual-anual;
		System.out.println("Su edad es:"+edad);
		
		int meses=edad*12;
		System.out.println("Número de meses:"+meses);
		
		int dias=edad*365;
		System.out.printf("Número de dias: %,d%n",dias);
		
		int horas=dias*24;
		System.out.printf("Número de horas: %,d%n",horas);
		
		int minutos=horas*60;
		System.out.printf("Número de minutos: %,d%n",minutos);
		
		c.close();
		
			
		
		
		
		
		
		
		
		
		
	}

}
