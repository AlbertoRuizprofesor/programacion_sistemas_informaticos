package interfacesGraficas;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class EjemploKeyListener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Ejemplo KeyListener");
        frame.setLayout(new FlowLayout()); // Añadimos un layout para que el campo no ocupe toda la ventana

        JTextField textField = new JTextField(20);

        // Registrar el escuchador usando KeyAdapter
        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                // e.getKeyChar() obtiene el carácter (letra, número)
                // e.getKeyCode() obtiene el código físico de la tecla (Esc, Enter, Flechas)
                System.out.println("Tecla física (Code): " + e.getKeyCode() + 
                                   " | Carácter: " + e.getKeyChar());
                
                // Ejemplo: Detectar si se pulsa la tecla ENTER
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    System.out.println("¡Has pulsado Enter!");
                }
            }
        });

        frame.add(new JLabel("Escribe algo:"));
        frame.add(textField);
        
        frame.setSize(300, 200);
        frame.setLocationRelativeTo(null); // Centrar ventana
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}