package interfacesGraficas;

import javax.swing.*;

public class EjemploJFrameJPanel {
    public static void main(String[] args) {
        JFrame ventana = new JFrame("Ejemplo con JPanel");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setSize(300, 200);

        JPanel panel = new JPanel();
        JLabel etiqueta = new JLabel("Hola desde el panel");

        panel.add(etiqueta);
        ventana.add(panel);

        ventana.setVisible(true);
    }
}
