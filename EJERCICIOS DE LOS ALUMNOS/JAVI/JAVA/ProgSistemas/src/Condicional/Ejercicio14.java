package Condicional;

/*Lee una temperatura y muestra:
•	< 0: “Helada”
•	0–15: “Fría”
•	16–25: “Templada”
•	25: “Calor”
*/

import java.util.Scanner;

public class Ejercicio14 {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Introduzca la temperatura en Grados: ");
		
		int temp = teclado.nextInt();
		
		if (temp < 0) {
			System.out.print("Menor que 0. Helada");
		} else if (temp >= 0 && temp <= 15) {
			System.out.print("0-15: Fría");
		} else if (temp >= 16 && temp <= 25) {
			System.out.print("16-25: Bien");
		} else if (temp > 25) {
			System.out.print("Calor");				
			
		}

	}

}
