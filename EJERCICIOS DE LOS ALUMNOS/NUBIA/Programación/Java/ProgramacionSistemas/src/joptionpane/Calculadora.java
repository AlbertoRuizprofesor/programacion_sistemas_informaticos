package joptionpane;
import javax.swing.JOptionPane;

public class Calculadora {

	    public static void main(String[] args) {
	        // 1. Entrada del primer número
	        String n1 = JOptionPane.showInputDialog("Introduce el primer número:");
	        double num1 = Double.parseDouble(n1); //para pasar de tipo String a double

	        // 2. Entrada del segundo número
	        String n2 = JOptionPane.showInputDialog("Introduce el segundo número:");
	        double num2 = Double.parseDouble(n2);

	        // 3. Realizar las operaciones
	        double suma = num1 + num2;
	        double resta = num1 - num2;
	        double multi = num1 * num2;
	        
	        // División por cero
	        String divTexto;
	        if (num2 != 0) {
	            divTexto = String.valueOf(num1 / num2);
	        } else {
	            divTexto = "Error (división por cero)";
	        }

	        // 4. Mostrar los resultados 
	        String mensaje = "Resultados para " + num1 + " y " + num2 + ":\n" +
	                         "\nSuma: " + suma +
	                         "\nResta: " + resta +
	                         "\nMultiplicación: " + multi +
	                         "\nDivisión: " + divTexto;

	        JOptionPane.showMessageDialog(null, mensaje, "Calculadora Java", JOptionPane.INFORMATION_MESSAGE);
	    }
	}
