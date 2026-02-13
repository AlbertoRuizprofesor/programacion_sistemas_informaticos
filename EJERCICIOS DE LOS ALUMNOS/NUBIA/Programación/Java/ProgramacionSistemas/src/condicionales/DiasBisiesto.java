package condicionales;
import java.time.YearMonth;
import java.util.Scanner;

public class DiasBisiesto {
	    public static void main(String[] args) {
	    	Scanner sc = new Scanner(System.in);
	        
	        System.out.print("Introduce el mes (1-12) y el año: ");
	        int mes = sc.nextInt(), año = sc.nextInt();

	        if (mes < 1 || mes > 12) {
	            System.out.println("ERROR: mes inválido");
	        } else {
	            int dias = YearMonth.of(año, mes).lengthOfMonth();
	            System.out.println("Días: " + dias);
	        }
	        sc.close();
	    }
	}
