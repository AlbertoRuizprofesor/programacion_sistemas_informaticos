package condicionales;
import java.util.Scanner;

public class NumeroPositivoNegativoCero {
	public static void main(String[] args) {
	Scanner c=new Scanner(System.in);
		
	System.out.print("Introduce un número: ");
	int numero = c.nextInt();
	
	if (numero<0) {
		System.out.print("El número es negativo.");
	}
	else if (numero==0) {
		System.out.print("El número es 0.");
	}
	else if (numero >0) {
		System.out.print("El número es positivo.");
	}
	c.close();
	}

}
