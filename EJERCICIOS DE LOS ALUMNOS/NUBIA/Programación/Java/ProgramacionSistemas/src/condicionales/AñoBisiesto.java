package condicionales;
import java.util.Scanner;

public class AñoBisiesto {
	public static void main(String[] args) { 

		Scanner sc = new Scanner(System.in); 

	    System.out.print("Introduce un año: "); 

	    int year = sc.nextInt(); 

	    boolean bisiesto = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0); 

	    System.out.println(bisiesto ? "Bisiesto" : "No bisiesto"); 

	    sc.close(); 
	  } 
} 

