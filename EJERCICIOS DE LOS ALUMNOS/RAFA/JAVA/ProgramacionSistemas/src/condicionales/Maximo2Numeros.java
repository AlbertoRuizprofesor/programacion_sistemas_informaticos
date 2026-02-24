package condicionales;
import java.util.Scanner;

public class Maximo2Numeros {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	    Scanner c = new Scanner(System.in);
	    System.out.print("A: ");
	    int a = c.nextInt();
	    System.out.print("B: ");
	    int b = c.nextInt();
	    
	    if (a > b) {
	        System.out.println("Mayor: " + a);
	      } else if (b > a) {
	        System.out.println("Mayor: " + b);
	      } else {
	        System.out.println("Son iguales");
	      }
	      c.close();



	}

}
