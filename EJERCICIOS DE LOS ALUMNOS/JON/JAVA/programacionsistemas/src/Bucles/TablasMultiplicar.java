package Bucles;
import java.util.Scanner;

public class TablasMultiplicar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	System.out.println("Tabla de Multiplicar bucle For");
	Scanner c=new Scanner(System.in);
	System.out.println("Introduce un número del 0 al 10:  ");
	int num=c.nextInt();
	System.out.println("La tabla de multiplicar de: " + num);
	for (int i=0;i<=10;i++) {
		System.out.println(i +" x " +num +" = " + (i*num));
	}
	
	
	System.out.println("---------------------------------------------");
	System.out.println("Tabla de Multiplicar bucle While");
	System.out.println("Introduce un número del 0 al 10:  ");
	int n=c.nextInt();
	System.out.println("La tabla de multiplicar de: " + n);
	int j=0;
	while (j<=10) {
		System.out.println(j +" x " +n +" = " + (j*n));
		j++;
	}
	
		
	System.out.println("---------------------------------------------");
	System.out.println("Tabla de Multiplicar bucle Do While");
	System.out.println("Introduce un número del 0 al 10:  ");
	int nm=c.nextInt();
	System.out.println("La tabla de multiplicar de: " + nm);
	int k=0;
	do {
		System.out.println(k +" x " +nm +" = " + (k*nm));
		k++;
	}while (k<=10);
		
	}
}


