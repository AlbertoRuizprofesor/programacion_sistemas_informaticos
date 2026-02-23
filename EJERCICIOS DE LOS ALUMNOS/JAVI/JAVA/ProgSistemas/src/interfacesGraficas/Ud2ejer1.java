package interfacesGraficas;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener; // Importante para capturar los clics

public class Ud2ejer1 {
    public static void main(String[] args) {
        // Crear el marco principal
        JFrame frame = new JFrame("FlowLayout con Eventos");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLocationRelativeTo(null); // Centra la ventana en la pantalla

        // Crear el panel con FlowLayout
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());

        // Crear los botones
        JButton button1 = new JButton("Botón 1");
        JButton button2 = new JButton("Botón 2");
        JButton button3 = new JButton("Botón 3");
        JButton button4 = new JButton("Botón 4");
        JButton button5 = new JButton("Botón 5");

        // --- Agregar lógica a los botones ---

        button1.addActionListener(e -> JOptionPane.showMessageDialog(frame, "¡Hola! Has pulsado el Botón 1"));
        
        button2.addActionListener(e -> JOptionPane.showMessageDialog(frame, "Este es el mensaje del Botón 2", "Aviso", JOptionPane.INFORMATION_MESSAGE));
        
        button3.addActionListener(e -> JOptionPane.showMessageDialog(frame, "¡Cuidado! Mensaje del Botón 3", "Advertencia", JOptionPane.WARNING_MESSAGE));
        
        button4.addActionListener(e -> JOptionPane.showMessageDialog(frame, "Error en el sistema del Botón 4", "Error", JOptionPane.ERROR_MESSAGE));
        
        button5.addActionListener(e -> JOptionPane.showMessageDialog(frame, "¿Sabías que el Botón 5 es el último?", "Curiosidad", JOptionPane.QUESTION_MESSAGE));

        // Añadir los botones al panel
        panel.add(button1);
        panel.add(button2);
        panel.add(button3);
        panel.add(button4);
        panel.add(button5);

        // Añadir el panel al marco y mostrar
        frame.add(panel);
        frame.setVisible(true);
    }
}