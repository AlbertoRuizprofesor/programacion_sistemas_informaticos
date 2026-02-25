package metodos;
import java.util.Scanner;


public class Calculadora {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//crear scanner
		Scanner c=new Scanner(System.in);
		//pedir datos por consola
		System.out.println("introduce numero 1:");
		int numero1=c.nextInt();
		System.out.println("introduce numero 2:");
		int numero2=c.nextInt();
		
		//operaciones
		EjercicioMetodo4 ejer4=new EjercicioMetodo4();
		System.out.println("la suma es: "+ejer4.sumar(numero1,numero2));
		System.out.println("la resta es: "+ejer4.restar(numero1,numero2));
		System.out.println("la multiplicacion es: "+ejer4.multi(numero1,numero2));
		System.out.println("la division es: "+ejer4.dividir(numero1,numero2));
		c.close();
		
		
		
		
	}
}
