package condicionales;
import java.util.Scanner; 

public class Max2Numeros {
	public static void main(String[] args) {
		Scanner c=new Scanner(System.in);
	
	System.out.println("COMPARADOR DE NÚMEROS");
	
	System.out.print("Introduce el primer número: ");
	int numero1 = c.nextInt();
	
	System.out.print("Introduce el segundo número: ");
	int numero2 = c.nextInt();
	
	if (numero1 == numero2) {
		System.out.print("Ambos números valen "+numero1);
	}
	else if (numero1 > numero2) {
		System.out.print(numero1+" es mayor que "+numero2);
	}
	else {
		System.out.print(numero1+" es menor que "+numero2);
	}
	
	c.close();
}
}