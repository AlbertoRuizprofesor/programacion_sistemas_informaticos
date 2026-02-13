package metodos;
import java.util.Scanner;

public class Operaciones {
	
	public int sumar(int numero1, int numero2) {
		return numero1+numero2;
	}
	public int restar(int numero1, int numero2) {
		return numero1-numero2;	
	}
	public int multi(int numero1, int numero2) {
		return numero1*numero2;
	}	
	public double divi(int numero1, int numero2) {
		return numero1/numero2;	
	}
	public int media(int numero1, int numero2) {
		return sumar(numero1, numero2)/2;
	}
	public void listaOperaciones(int numero1,int numero2 ) {
		String []nombreOpera= {"Suma", "Resta", "Multiplicación", "División", "Media"};
		double [] op= {sumar(numero1, numero2), restar(numero1, numero2), multi(numero1, numero2), divi(numero1, numero2), media(numero1, numero2)};
		
		int i=0;
		for (double numer:op) {
			System.out.println(" · La "+nombreOpera[i]+ " es "+ numer);
			i++;
		}	
	}
	public int[] pedirDatos() {
		Scanner c=new Scanner(System.in);
		int [] numero=new int[2];
		
		for (int i=0;i<numero.length;i++) {
			System.out.print("Dime el numero "+(i+1)+": ");
			numero[i]=c.nextInt();
		}
		
		c.close();
		return numero;
	}
}

