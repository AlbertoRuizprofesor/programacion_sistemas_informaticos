package interfacesGraficas;


import javax.swing.*;
import java.awt.*;

public class Ejercicio3 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Ventana3");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 150);

        JPanel panel = new JPanel(new FlowLayout());

        panel.add(new JButton("Uno"));
        panel.add(new JButton("Dos"));
        panel.add(new JButton("Tres"));
        panel.add(new JButton("Cuatro"));
        panel.add(new JButton("Cinco"));
        panel.add(new JButton("Seis"));

        frame.add(panel);
        frame.setVisible(true);
    }
}
