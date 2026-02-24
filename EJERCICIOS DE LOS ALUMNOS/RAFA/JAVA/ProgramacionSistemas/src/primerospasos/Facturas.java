package primerospasos;
import java.util.Scanner;

public class Facturas {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c=new Scanner(System.in);
		System.out.println("indica el importe");
		double importe=c.nextDouble();
		System.out.println("indica las unidades");
		int unidades=c.nextInt();
		
		double total=unidades*importe;
		System.out.printf("el total es:%.2f %n",total);
		double descuento=total*0.10;
		System.out.printf("el total - descuento es:%.2f %n ",descuento);
		double base_imponible=total-descuento;
		System.out.printf("la base imponible es:%.2f %n ",base_imponible);
		double iva=base_imponible*0.21;
		System.out.printf("el iva es: %.2f %n",iva);
		double total_pagar=base_imponible+iva;
		System.out.printf("el total a pagar es : %.2f %n ",total_pagar);
		
		c.close();

	}

}
