package interfacesGraficas;

import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

public class Ejercicio4 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("BorderLayout");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new BorderLayout());

        frame.add(new JButton("Norte"), BorderLayout.NORTH);
        frame.add(new JButton("Sur"), BorderLayout.SOUTH);
        frame.add(new JButton("Este"), BorderLayout.EAST);
        frame.add(new JButton("Oeste"), BorderLayout.WEST);
        frame.add(new JButton("Centro"), BorderLayout.CENTER);

        frame.setVisible(true);
    }

}
