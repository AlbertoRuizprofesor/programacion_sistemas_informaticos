package Condicionales;
import java.util.Scanner;

public class EjercicioImportesDescuento {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		Scanner c=new Scanner(System.in);
		System.out.printf("Introduce el importe:  ");
		double importe=c.nextDouble();
		System.out.printf("Introduce las unidades: ");
		int cantidad=c.nextInt();
		double total,desc,iva,totalf,descuento = 0;
		total=importe*cantidad;
		
		if (total>0 && total<=100) {
			descuento=0;
			
		} else if (total>101 && total<=1000) {
			descuento=10;
			
		} else if (total>1000) {
			descuento=20;
			
		}
		
		
		desc=total-(total*descuento/100);
		iva=desc*0.21;
		totalf=desc+iva;
		
		System.out.println("El importe total es: " + String.format ("%.2f",total));
		System.out.println("El total con descuento es: " + String.format ("%.2f",desc));
		System.out.println("El iva de ese importe es: " + String.format ("%.2f",iva));
		System.out.println("El total de factura es: " + String.format ("%.2f",totalf));
			
		c.close();
	}

}
