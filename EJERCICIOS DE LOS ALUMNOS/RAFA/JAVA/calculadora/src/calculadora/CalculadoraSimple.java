package calculadora;

import javax.swing.*;
import java.awt.*;

public class CalculadoraSimple extends JFrame {

    private JTextField operador1, operador2, resultado;

    public CalculadoraSimple() {
        // Configuración de la ventana
        setTitle("Calculadora Simple");
        setSize(450, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(5, 1, 5, 5));

        // --- Campos de entrada ---
        JPanel panelCampos = new JPanel(new FlowLayout());
        panelCampos.add(new JLabel("Operador 1:"));
        operador1 = new JTextField(8);
        panelCampos.add(operador1);
        panelCampos.add(new JLabel("Operador 2:"));
        operador2 = new JTextField(8);
        panelCampos.add(operador2);
        add(panelCampos);

        // --- Botones de suma y resta ---
        JPanel panelSumaResta = new JPanel(new FlowLayout());
        JButton sumar = new JButton("Sumar");
        JButton restar = new JButton("Restar");
        panelSumaResta.add(sumar);
        panelSumaResta.add(restar);
        add(panelSumaResta);

        // --- Botones de multiplicar y dividir ---
        JPanel panelMultiDiv = new JPanel(new FlowLayout());
        JButton multiplicar = new JButton("Multiplicar");
        JButton dividir = new JButton("Dividir");
        panelMultiDiv.add(multiplicar);
        panelMultiDiv.add(dividir);
        add(panelMultiDiv);

        //--- Botones de potencia y raíz ---
        JPanel panelPotencias = new JPanel(new FlowLayout());
        JButton potencia1 = new JButton("Potencia Op1");
        JButton potencia2 = new JButton("Potencia Op2");
        JButton raiz1 = new JButton("Raíz Op1");
        JButton raiz2 = new JButton("Raíz Op2");
        panelPotencias.add(potencia1);
        panelPotencias.add(potencia2);
        panelPotencias.add(raiz1);
        panelPotencias.add(raiz2);
        add(panelPotencias);

        // --- Resultado y limpiar ---
        JPanel panelResultado = new JPanel(new FlowLayout());
        panelResultado.add(new JLabel("Resultado:"));
        resultado = new JTextField(10);
        resultado.setEditable(false);
        panelResultado.add(resultado);
        JButton limpiar = new JButton("Limpiar");
        panelResultado.add(limpiar);
        add(panelResultado);

        // --- Eventos ---
        sumar.addActionListener(e -> calcular("+"));
        restar.addActionListener(e -> calcular("-"));
        multiplicar.addActionListener(e -> calcular("*"));
        dividir.addActionListener(e -> calcular("/"));
        potencia1.addActionListener(e -> calcular("^1"));
        potencia2.addActionListener(e -> calcular("^2"));
        raiz1.addActionListener(e -> calcular("√1"));
        raiz2.addActionListener(e -> calcular("√2"));
        limpiar.addActionListener(e -> {
            operador1.setText("");
            operador2.setText("");
            resultado.setText("");
        });
    }

    private void calcular(String operacion) {
        try {
            double op1 = 0, op2 = 0;

            // Leer solo los campos necesarios según la operación
            if (!operacion.equals("^2") && !operacion.equals("√2")) {
                op1 = Double.parseDouble(operador1.getText());
            }
            if (!operacion.equals("^1") && !operacion.equals("√1")) {
                op2 = Double.parseDouble(operador2.getText());
            }

            double res = 0;
            switch (operacion) {
                case "+": res = op1 + op2; break;
                case "-": res = op1 - op2; break;
                case "*": res = op1 * op2; break;
                case "/": 
                    if(op2 == 0) {
                        JOptionPane.showMessageDialog(this, "No se puede dividir entre 0");
                        return;
                    }
                    res = op1 / op2; 
                    break;
                case "^1": res = Math.pow(op1, 2); break;
                case "^2": res = Math.pow(op2, 2); break;
                case "√1": 
                    if(op1 < 0) { JOptionPane.showMessageDialog(this, "Raíz no válida"); return; }
                    res = Math.sqrt(op1); 
                    break;
                case "√2": 
                    if(op2 < 0) { JOptionPane.showMessageDialog(this, "Raíz no válida"); return; }
                    res = Math.sqrt(op2); 
                    break;
            }
            resultado.setText(String.valueOf(res));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Ingresa valores numéricos válidos");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            CalculadoraSimple calc = new CalculadoraSimple();
            calc.setVisible(true);
        });
    }
}