package Bucles;
import java.util.Scanner;

public class Ejercicio3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(" Suma de 1..N");
		Scanner c=new Scanner(System.in);
		System.out.printf("Introduce el número que desees: ");
		int cont=c.nextInt();
		int suma=0 ;
		for (int i=0 ; i<=cont ; i++) {
			suma+=i;
			;
		}
		System.out.println(suma);

	}

}