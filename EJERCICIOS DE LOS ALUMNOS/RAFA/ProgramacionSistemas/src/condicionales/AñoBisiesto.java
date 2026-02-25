package condicionales;
import java.util.Scanner;

public class AñoBisiesto {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	    Scanner c = new Scanner(System.in);
	    System.out.print("Año: ");
	    int year = c.nextInt();

	    boolean bisiesto = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
	    System.out.println(bisiesto ? "Bisiesto" : "No bisiesto");

	    c.close();

	}

}
