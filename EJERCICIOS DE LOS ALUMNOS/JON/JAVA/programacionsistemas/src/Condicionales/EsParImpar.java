package Condicionales;
import java.util.Scanner;

public class EsParImpar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		Scanner c=new Scanner(System.in);
		System.out.println("Introduce un número entero:  ");
		int numero=c.nextInt();
		if (numero % 2==0) {
			// espar
			System.out.println("El número introducido es par.");
		}else {
			// esimpar
			System.out.println("El número introducido es impar.");
		}

	}

}
