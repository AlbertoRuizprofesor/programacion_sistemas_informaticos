package condicionales;
import java.util.Scanner;

public class Importe {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c=new Scanner(System.in);
		System.out.print("Dime un importe:");
		int importe=c.nextInt();
		System.out.println("importe es:"+importe);
		//operaciones
		double descuento1=importe*0.10;
		double descuento2=importe*0.20;
		//condicionales
		if(importe>0 && importe<=100) {
			System.out.print("el importe menos el descuento es: "+importe);
		}else if(importe>100 && importe<=1000) {
			System.out.print("el importe menos el 10% de descuento es: "+(importe-descuento1));
		}else if(importe>1000) {
			System.out.print("el importe menos el 20% de descuento es: "+(importe-descuento2));
		}else {
			System.out.print("no se introducir menor que 0" );
		}
		
		c.close();
	}

}
