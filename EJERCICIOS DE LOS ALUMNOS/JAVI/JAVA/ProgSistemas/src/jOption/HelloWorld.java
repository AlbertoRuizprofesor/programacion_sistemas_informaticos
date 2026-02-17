import javax.swing.JOptionPane;

public class CalculadoraExpress {
    public static void main(String[] args) {
        // 1. Selección de operación
        String[] opciones = {"Sumar", "Restar", "Multiplicar", "Dividir", "Salir"};
        int seleccion = JOptionPane.showOptionDialog(null, "Selecciona una operación:",
                "Calculadora Java", JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE,
                null, opciones, opciones[0]);

        // Si el usuario cierra la ventana o elige "Salir"
        if (seleccion == 4 || seleccion == -1) {
            JOptionPane.showMessageDialog(null, "¡Hasta luego!");
            System.exit(0);
        }

        try {
            // 2. Entrada de datos
            double num1 = Double.parseDouble(JOptionPane.showInputDialog("Introduce el primer número:"));
            double num2 = Double.parseDouble(JOptionPane.showInputDialog("Introduce el segundo número:"));
            double resultado = 0;
            String operacion = "";

            // 3. Lógica de cálculo
            switch (seleccion) {
                case 0: // Sumar
                    resultado = num1 + num2;
                    operacion = "Suma";
                    break;
                case 1: // Restar
                    resultado = num1 - num2;
                    operacion = "Resta";
                    break;
                case 2: // Multiplicar
                    resultado = num1 * num2;
                    operacion = "Multiplicación";
                    break;
                case 3: // Dividir
                    if (num2 == 0) {
                        JOptionPane.showMessageDialog(null, "Error: No se puede dividir por cero.", "Error", JOptionPane.ERROR_MESSAGE);
                        return;
                    }
                    resultado = num1 / num2;
                    operacion = "División";
                    break;
            }

            // 4. Mostrar resultado
            JOptionPane.showMessageDialog(null, "El resultado de la " + operacion + " es: " + resultado);

        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Error: Por favor, introduce solo números válidos.", "Error de formato", JOptionPane.ERROR_MESSAGE);
        }
    }
}