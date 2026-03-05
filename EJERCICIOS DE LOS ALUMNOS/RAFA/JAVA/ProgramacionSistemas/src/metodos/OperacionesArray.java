
package metodos;

import java.util.Scanner;

public class OperacionesArray {
		
	public int sumar(int numero1, int numero2) {
		return numero1+numero2;	
	}
	
	public int restar(int numero1, int numero2) {
		return numero1-numero2;	
	}

	public int multiplicacion(int numero1, int numero2) {
		return numero1*numero2;	
	}

	public double division(int numero1, int numero2) {
		return numero1/numero2;	
	}
	
	public void lista_Operaciones(int numero1,int numero2 ) {
		String []nombre_opera= {"Suma","Resta","multiplicación","División"}; 
		double [] op= {sumar(numero1,numero2),restar(numero1,numero2),
				multiplicacion(numero1,numero2),division(numero1,numero2)};
	
		
		int i=0;
		for (double numer:op) {
			
			System.out.println(" la "+nombre_opera[i]+ " es: "+ numer);
			i++;
		}
			
	}
	
	public int[] pedirDatos() {
		Scanner c=new Scanner(System.in);
		int [] numero=new int[4];
		
		for (int i=0;i<numero.length;i++) {
			System.out.print("Dime el numero "+(i+1)+" : ");
			numero[i]=c.nextInt();
		}
		
		c.close();
		return numero;
		
		
	}
}



/*

package metodos;
import jav.util.Scanner;
public class Operaciones{
	public int sumar(int numero1, int numero2) {
		return numero1 + numero2;
	}
	public void lista_Operaciones(int numero1, int numero2){
		double [] operacion=new double[4];
		String [] nombre_opera= {"suma","resta",multiplicacion","division"};
		operacion[0]=sumar(numero1,numero2);
		operacion[1]=
		operacion[2]=
		operacion[3]=
		
		int i=0;
		for (double numer:op){
			System.out.println("la "+nombre_opera[i]+ " es: "+numer);
			i++;
	}
}

*/