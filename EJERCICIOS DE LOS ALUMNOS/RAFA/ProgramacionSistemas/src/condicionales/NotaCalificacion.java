package condicionales;
import java.util.Scanner;

public class NotaCalificacion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	    Scanner c = new Scanner(System.in);
	    System.out.print("Nota (0-10): ");
	    double nota = c.nextDouble();
	    
	    if (nota < 0 || nota > 10) {
	        System.out.println("ERROR: nota fuera de rango");
	      } else if (nota < 5) {
	        System.out.println("Suspenso");
	      } else if (nota < 7) {
	        System.out.println("Aprobado");
	      } else if (nota < 9) {
	        System.out.println("Notable");
	      } else {
	        System.out.println("Sobresaliente");
	      }
	      c.close();



	}

}
