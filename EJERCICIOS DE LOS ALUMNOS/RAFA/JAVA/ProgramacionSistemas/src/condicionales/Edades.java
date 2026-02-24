package condicionales;
import java.util.Scanner;

public class Edades {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c=new Scanner(System.in);
		System.out.print("Dime tu año de nacimiento:");
		int anual=c.nextInt();
		int actual=2026;
		
		int edad=actual-anual;
		System.out.println("Su edad es:"+edad);
		
		if (edad<18) {
			System.out.print("eres menor de edad en España");
		}else {
			System.out.print("eres mayor de edad en España");
		}
		
		c.close();

	}

}
