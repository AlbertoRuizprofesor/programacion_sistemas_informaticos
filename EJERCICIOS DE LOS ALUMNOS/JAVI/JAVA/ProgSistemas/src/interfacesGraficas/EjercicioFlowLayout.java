package interfacesGraficas;

import javax.swing.*;
import java.awt.*;

public class EjercicioFlowLayout {
    public static void main(String[] args) {
        // 1. Configuración del marco
        JFrame frame = new JFrame("FlowLayout Exercise");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(810, 200); // Ventana ancha para que todo quepa en una línea
        frame.setLocationRelativeTo(null);

        // 2. Panel con FlowLayout alineado a la izquierda (o CENTRADO según prefieras)
        // El espacio de 10px ayuda a que no estén pegados
        JPanel panel = new JPanel(new FlowLayout(FlowLayout.LEFT, 10, 20));

        // --- GRUPO 1: NOMBRE ---
        JLabel lblNombre = new JLabel("Nombre:");
        JTextArea txtNombre = new JTextArea(2, 8); // 2 filas, 8 columnas
        txtNombre.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY));
        JButton btnNombre = new JButton("Validar nombre");

        // --- GRUPO 2: EMAIL ---
        JLabel lblEmail = new JLabel("Email:");
        JTextArea txtEmail = new JTextArea(2, 8);
        txtEmail.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY));
        JButton btnEmail = new JButton("Validar email");

        // --- GRUPO 3: NIF ---
        JLabel lblNif = new JLabel("Nif:");
        JTextArea txtNif = new JTextArea(2, 8);
        txtNif.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY));
        JButton btnNif = new JButton("Validar Nif");

        // 3. Añadir al panel en el orden exacto de la imagen
        panel.add(lblNombre);
        panel.add(txtNombre);
        panel.add(btnNombre);

        panel.add(lblEmail);
        panel.add(txtEmail);
        panel.add(btnEmail);

        panel.add(lblNif);
        panel.add(txtNif);
        panel.add(btnNif);

        // 4. Lógica de validación (opcional, usando lo que vimos antes)
        btnEmail.addActionListener(e -> {
            String email = txtEmail.getText().trim();
            if (email.matches("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$")) {
                JOptionPane.showMessageDialog(frame, "Email válido");
            } else {
                JOptionPane.showMessageDialog(frame, "Email NO válido", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        // Hacer visible
        frame.add(panel);
        frame.setVisible(true);
    }
}