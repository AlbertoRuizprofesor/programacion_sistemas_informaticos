package condicionales;

public class Importe {
	public static void main(String[] args) {
		
		System.out.println("INDICADOR DE DESCUENTO");
		
		int importe=200;
		System.out.println("El importe es "+importe);
				
		if (importe>=0 && importe<=100) {
			System.out.print("No se aplica descuento");
		}
		else if (importe>=100 && importe<=1000) {
			System.out.println("Se aplica un 10% de descuento");
			int descuento1=importe - importe*10/100;
			System.out.print("El importe final es "+descuento1);
	
		}
		else if (importe>1000) {
			System.out.println("Se aplica un 20% de descuento");
			int descuento2= importe - importe*20/100 ;
			System.out.print("El importe final es "+descuento2);
		}
	}
}
