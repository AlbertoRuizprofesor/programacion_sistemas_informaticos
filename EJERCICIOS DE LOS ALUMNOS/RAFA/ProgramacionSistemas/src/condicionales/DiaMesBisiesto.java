package condicionales;
import java.util.Scanner;

public class DiaMesBisiesto {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner c = new Scanner(System.in);
	    System.out.print("Mes (1-12): ");
	    int mes = c.nextInt();
	    System.out.print("Año: ");
	    int year = c.nextInt();

	    if (mes < 1 || mes > 12) {
	        System.out.println("ERROR: mes inválido");
	        c.close();
	        return;
	      }

	      int dias;
	      switch (mes) {
	        case 4, 6, 9, 11 -> dias = 30;
	        case 2 -> {
	          boolean bisiesto = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
	          dias = bisiesto ? 29 : 28;
	        }
	        default -> dias = 31;
	      }

	      System.out.println("Días: " + dias);
	      c.close();

	}

}
