package primerospasos;
import java.util.Scanner;

public class CalcularIVA {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner c=new Scanner(System.in);
		System.out.println("Introduce el importe: ");
		double importe=c.nextDouble();
			
		double iva;
		iva=importe*0.21;
		
		System.out.println("El importe a calcular es: "+importe);
		System.out.println("El iva de ese importe es: "+iva);
		
			
		c.close();
	}

}
