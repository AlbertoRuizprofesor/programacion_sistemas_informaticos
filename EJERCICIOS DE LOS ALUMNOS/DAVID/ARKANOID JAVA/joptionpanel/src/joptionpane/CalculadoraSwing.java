package joptionpane;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraSwing extends JFrame implements ActionListener {
    private JTextField pantalla;
    private double resultado = 0;
    private String ultimaOperacion = "=";
    private boolean principio = true;

    public CalculadoraSwing() {
        setTitle("Calculadora Java con Borrar");
        setSize(300, 450); // Un poco más alta para el nuevo botón
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        pantalla = new JTextField("0");
        pantalla.setEditable(false);
        pantalla.setHorizontalAlignment(JTextField.RIGHT);
        pantalla.setFont(new Font("Arial", Font.BOLD, 24));
        add(pantalla, BorderLayout.NORTH);

        JPanel panelBotones = new JPanel();
        // Cambiamos a 5 filas para que el botón C tenga su espacio
        panelBotones.setLayout(new GridLayout(5, 4, 5, 5));

        String[] botones = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C", "", "", "" // Añadimos el botón C y espacios vacíos
        };

        for (String texto : botones) {
            if (texto.equals("")) {
                panelBotones.add(new JLabel("")); // Espacio vacío estético
            } else {
                JButton boton = new JButton(texto);
                boton.setFont(new Font("Arial", Font.PLAIN, 18));
                if (texto.equals("C")) boton.setForeground(Color.RED); // Resaltar el borrar
                boton.addActionListener(this);
                panelBotones.add(boton);
            }
        }

        add(panelBotones, BorderLayout.CENTER);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String comando = e.getActionCommand();

        // Lógica para el botón de borrar
        if (comando.equals("C")) {
            resultado = 0;
            ultimaOperacion = "=";
            principio = true;
            pantalla.setText("0");
            return;
        }

        // Si es un número o punto
        if ((comando.charAt(0) >= '0' && comando.charAt(0) <= '9') || comando.equals(".")) {
            if (principio) {
                pantalla.setText(comando);
                principio = false;
            } else {
                pantalla.setText(pantalla.getText() + comando);
            }
        } else {
            // Si es una operación
            calcular(Double.parseDouble(pantalla.getText()));
            ultimaOperacion = comando;
            principio = true;
        }
    }

    private void calcular(double x) {
        switch (ultimaOperacion) {
            case "+": resultado += x; break;
            case "-": resultado -= x; break;
            case "*": resultado *= x; break;
            case "/": 
                if (x == 0) pantalla.setText("Error");
                else resultado /= x; 
                break;
            case "=": resultado = x; break;
        }
        pantalla.setText("" + resultado);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new CalculadoraSwing());
    }
}