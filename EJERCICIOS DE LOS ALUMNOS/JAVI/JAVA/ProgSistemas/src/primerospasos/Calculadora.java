package primerospasos;

import java.util.Scanner;

public class Calculadora {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        
        System.out.print("Introduce un número: ");
        float num1 = teclado.nextFloat();
        
        
        System.out.print("Introduce otro número: ");
        float num2 = teclado.nextFloat();
        
       
        System.out.print("Introduce la operación ( + , - , * , / ): ");
        String operacion = teclado.nextLine();
        
        
        if (operacion.equals("+")) {
            System.out.println("Resultado: " + (num1 + num2));
        } else if (operacion.equals("-")) {
        	
            System.out.println("Resultado: " + (num1 - num2));
        } else if (operacion.equals("*")) {
        	
        	System.out.println("Resultado: " + (num1 * num2));
        } else if (operacion.equals("/")) {
        	
        	System.out.println("Resultado: " + (num1 / num2));
        } else {
        	
        	System.out.println("Operacion no válida");
        }
        
        teclado.close();
    }
}

