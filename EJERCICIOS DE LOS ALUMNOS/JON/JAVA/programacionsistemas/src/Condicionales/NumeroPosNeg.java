package Condicionales;
import java.util.Scanner;

public class NumeroPosNeg {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c=new Scanner(System.in);
		System.out.println("Introduce un número entero:  ");
		int num=c.nextInt();
		
		if (num<0) {
			System.out.println("El número es negativo.");
		} else if (num>0) {
			System.out.println("El número es positivo.");
		} else {
			System.out.println("El número introducido es cero.");
		}

	}

}
