package condicionales;

public class Edades {
	public static void main(String[] args) {
		
		int edad=65;
		
		if (edad<18) {
			System.out.print("Eres menor de edad");
		}
		else if (edad>=18 && edad<65) {
			System.out.print("Eres mayor de edad");
		}
		else if(edad>=65) {
			System.out.print("Eres un abuelete");
		}
		
	}
}