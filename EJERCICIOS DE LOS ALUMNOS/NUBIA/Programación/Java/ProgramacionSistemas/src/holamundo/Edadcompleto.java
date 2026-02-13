package holamundo;
import java.util.Scanner;

public class Edadcompleto {
	
	public static void main(String[] args) {
		Scanner c=new Scanner(System.in);
		
		System.out.println("Ingresa tu año de nacimiento: ");
		int anual= c.nextInt();
		int actual=2026;
		int edad= actual - anual;
		
		System.out.println();
		System.out.println("Año de nacimiento: "+anual);
		System.out.println("Año actual: "+actual);
		System.out.println("Su edad es: "+edad+ " años.");
		System.out.println("O lo que es lo mismo: ");
		
		int meses=edad*12;
		System.out.println("- Meses: "+meses);
		
		int dias=edad*12*365;
		System.out.println("- Días: "+dias);
		
		int horas=edad*12*365*24;
		System.out.println("- Horas: "+horas);
		
		int minutos=edad*12*365*24*60;
		System.out.println("- Minutos: "+minutos);
		
		
		
		
		c.close();
		
	}

}
