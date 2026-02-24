package ejerciciosObligatoriosMetodos;
import java.util.Scanner;

public class Calculadora {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s= new Scanner(System.in);
		
		System.out.print("indica el primer número; ");     
        int a=s.nextInt();
        System.out.print("indica el segundor número; ");   
        int b=s.nextInt();
        //invocamos los diferentes metodos
        System.out.println("Suma: " + suma(a, b));
        System.out.println("Resta: " + resta(a, b));
        System.out.println("Producto: " + producto(a, b));
        System.out.println("División: " + division(a, b));

	}
	
	//metodos static, no necesitan instanciar una clase.
	public static int suma(int a, int b){
		return a + b;
	}
	public static int resta(int a, int b) {
		return a-b;
	}
	public static int producto(int a,int b) {
		return a*b;
	}
	public static int division(int a, int b) {
		return a / b;
	}
}
