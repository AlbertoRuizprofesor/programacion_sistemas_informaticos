package Condicionales;
import java.util.Scanner;

public class EjercicioNotas {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner a=new Scanner(System.in);
		System.out.printf("Introduce la nota:  ");
		double nota=a.nextDouble();
		
		if (nota>=0 && nota<5) {
			System.out.print("Estás suspenso.");
		
		}else if (nota>=5 && nota<6) {
			System.out.print("Tienes un suficiente.");
			
		}else if (nota>=5 && nota<=6) {
			System.out.print("Tienes un Bien.");
			
		}else if (nota>=7 && nota<=8.50) {
			System.out.print("Tienes un Notable.");
			
		}else if (nota>8.50 && nota<=10) {
			System.out.print("Tienes un Sobresaliente.");
					
		}else {
			System.out.print("Nota fuera de rango.");
		}

	}

}
