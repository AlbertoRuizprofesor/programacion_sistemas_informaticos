package interfacesGraficas;

import javax.swing.*;
import java.awt.*;

public class EjercicioRadioButton6 extends JFrame {

    public EjercicioRadioButton6() {
        setTitle("Matrix");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // 1. Definimos los datos en arrays (Texto y Mensaje)
        String[] opciones = {"Pastilla Azul", "Pastilla Roja", "Pastilla Verde", "Pastilla Amarilla"};
        String[] mensajes = {
            "Has elegido la opción azul, quédate en tu mundo de fantasía.",
            "Has elegido la opción roja, te contaré la verdad sobre Matrix.",
            "Has elegido la opción verde, las pastillas de la abuela.",
            "Has elegido la opción amarilla, te comiste un caramelo."
        };

        // 2. Contenedores
        ButtonGroup group = new ButtonGroup();
        JPanel panel = new JPanel();
        // Opcional: Layout vertical para que no se amontonen
        panel.setLayout(new BoxLayout(panel, BoxLayout.X_AXIS));

        // 3. Bucle para crear, agrupar y añadir
        for (int i = 0; i < opciones.length; i++) {
            JRadioButton rb = new JRadioButton(opciones[i]);
            
            // Usamos una variable final para el índice dentro del Lambda
            final int index = i; 
            rb.addActionListener(e -> mostrarMensaje("Elección elegida", mensajes[index]));

            group.add(rb);    // Lógica (solo uno marcado)
            panel.add(rb);    // Vista (que aparezca en pantalla)
        }

        add(panel);
        pack();
        setLocationRelativeTo(null);
    }

    private void mostrarMensaje(String titulo, String mensaje) {
        JOptionPane.showMessageDialog(this, mensaje, titulo, JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new EjercicioRadioButton6().setVisible(true));
    }
}
