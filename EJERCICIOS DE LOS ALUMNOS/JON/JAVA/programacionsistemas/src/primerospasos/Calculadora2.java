package primerospasos;

import java.util.Scanner;

public class Calculadora2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//crear scanner
		Scanner c=new Scanner (System.in);
		//pedir datos por consola
		System.out.println("Introduce el número 1: ");
		int n1=c.nextInt();
		System.out.println("Introduce el número 2: ");
		int n2=c.nextInt();
		
		int suma, resta, multi,divi;
				
		suma=n1+n2;
		resta=n1-n2;
		multi=n1*n2;
		divi=n1/n2;
		System.out.println("La suma es: "+suma);
		System.out.println("La resta es: "+resta);
		System.out.println("La multiplicacion es: "+multi);
		System.out.println("La division es: "+divi);
		
		c.close();
		}


	}


