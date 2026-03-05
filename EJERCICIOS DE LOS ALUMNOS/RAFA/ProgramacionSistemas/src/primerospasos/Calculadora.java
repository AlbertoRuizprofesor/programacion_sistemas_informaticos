package primerospasos;
import java.util.Scanner;

public class Calculadora {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//crear scanner
		Scanner c=new Scanner(System.in);
		//pedir datos por consola
		System.out.println("introduce numero 1:");
		int numero1=c.nextInt();
		System.out.println("introduce numero 2:");
		int numero2=c.nextInt();
		
		//operaciones
		int suma,resta,multi,divi;
		suma=numero1+numero2;
		resta=numero1-numero2;
		multi=numero1*numero2;
		divi=numero1/numero2;
		
		//salir por pantalla
		System.out.println("la suma es "+suma);
		
		
		c.close();
		
		
		
		
	}

}
