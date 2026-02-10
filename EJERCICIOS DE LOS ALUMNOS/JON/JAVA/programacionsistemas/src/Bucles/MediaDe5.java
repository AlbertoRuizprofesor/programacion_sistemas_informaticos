package Bucles;
import java.util.Scanner;
public class MediaDe5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(" Media de 5");
		Scanner c=new Scanner(System.in);
		int suma=0 ;
		for (int i=0 ; i<5 ; i++) {
			System.out.println("Introduce el siguiente número: ");
			suma+=c.nextDouble();
		}
		System.out.println("La media es: " +(suma/5));
	}

}
