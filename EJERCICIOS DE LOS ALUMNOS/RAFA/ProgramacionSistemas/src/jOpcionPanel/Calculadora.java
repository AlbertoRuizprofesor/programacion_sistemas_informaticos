package jOpcionPanel;
import javax.swing.JOptionPane;

public class Calculadora {

    public static void main(String[] args) {

        // Pedir números
        String num1Str = JOptionPane.showInputDialog("Ingrese el primer número:");
        String num2Str = JOptionPane.showInputDialog("Ingrese el segundo número:");

        // Convertir a double
        double num1 = Double.parseDouble(num1Str);
        double num2 = Double.parseDouble(num2Str);

        // Menú de opciones
        String operacion = JOptionPane.showInputDialog(
                "Seleccione operación:\n" +
                "1 - Sumar\n" +
                "2 - Restar\n" +
                "3 - Multiplicar\n" +
                "4 - Dividir");

        double resultado = 0;
        String simbolo = "";

        switch (operacion) {
            case "1":
                resultado = num1 + num2;
                simbolo = "+";
                break;
            case "2":
                resultado = num1 - num2;
                simbolo = "-";
                break;
            case "3":
                resultado = num1 * num2;
                simbolo = "*";
                break;
            case "4":
                if (num2 != 0) {
                    resultado = num1 / num2;
                    simbolo = "/";
                } else {
                    JOptionPane.showMessageDialog(null, "No se puede dividir entre 0");
                    System.exit(0);
                }
                break;
            default:
                JOptionPane.showMessageDialog(null, "Opción inválida");
                System.exit(0);
        }

        // Mostrar resultado
        JOptionPane.showMessageDialog(null,
                "Resultado:\n" +
                num1 + " " + simbolo + " " + num2 + " = " + resultado);
    }
}
