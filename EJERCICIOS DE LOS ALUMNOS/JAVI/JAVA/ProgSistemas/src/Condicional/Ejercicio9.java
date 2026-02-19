import package Condicional;
		
		
		import java.util.Scanner;

		public class Ejercicio9 {
		    public static void main(String[] args) {
		        
		        Scanner teclado = new Scanner(System.in);
		        
		        System.out.print("Introduce el número 1: ");
		        int a = teclado.nextInt();
		        
		        System.out.print("Introduce el número 2: ");
		        int b = teclado.nextInt();
		        
		       
		        teclado.nextLine(); 
		        
		        System.out.print("Introduce el operador (+, -, *, /): ");
		     
		        String operador = teclado.nextLine();
		        
		       
		        if (operador.equals("+")) {
		            System.out.print("La suma es: " + (a + b));
		        } else if (operador.equals("-")) {
		            System.out.print("La resta es: " + (a - b));
		        } else if (operador.equals("*")) {
		            System.out.print("La multiplicación es: " + (a * b));
		        } else if (operador.equals("/")) {
		            if (b != 0) {
		                System.out.print("La división es: " + (a / b));
		            } else {
		                System.out.print("Error: No se puede dividir por cero.");
		            }
		        } else {
		            System.out.print("Operador no válido.");
		        }
		        
		        teclado.close();
		    }
		
		
		
				
				
				
				
	
	}


