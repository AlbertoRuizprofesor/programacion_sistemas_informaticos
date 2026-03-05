package condicionales;
import java.util.Scanner;

public class Maximo3Numeros {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner cc = new Scanner(System.in);
	    System.out.print("A: ");
	    int a = cc.nextInt();
	    System.out.print("B: ");
	    int b = cc.nextInt();
	    System.out.print("C: ");
	    int c = cc.nextInt();
	    
	    int max = a;
	    if (b > max) max = b;
	    if (c > max) max = c;

	    System.out.println("Mayor: " + max);
	    cc.close();



	}

}
