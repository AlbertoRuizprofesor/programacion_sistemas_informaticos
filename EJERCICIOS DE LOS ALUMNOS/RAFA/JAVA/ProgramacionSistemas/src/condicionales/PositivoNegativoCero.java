package condicionales;
import java.util.Scanner;

public class PositivoNegativoCero {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner c = new Scanner(System.in);
	    System.out.print("Número: ");
	    int n = c.nextInt();
	    
	    if (n > 0) {
	        System.out.println("Positivo");
	      } else if (n < 0) {
	        System.out.println("Negativo");
	      } else {
	        System.out.println("Cero");
	      }
	      c.close();


	}

}
