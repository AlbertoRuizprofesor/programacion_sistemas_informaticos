package condicionales;
import java.util.Scanner;

public class ParImpar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	    Scanner c = new Scanner(System.in);
	    System.out.print("Número: ");
	    int n = c.nextInt();

	    if (n % 2 == 0) {
	        System.out.println("Par");
	      } else {
	        System.out.println("Impar");
	      }
	      c.close();

	}

}
