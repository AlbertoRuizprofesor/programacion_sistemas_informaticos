package interfacesGraficas;

import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

public class Ejercicio5 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("GridLayout");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        frame.setLayout(new GridLayout(2, 3));

        frame.add(new JButton("1"));
        frame.add(new JButton("2"));
        frame.add(new JButton("3"));
        frame.add(new JButton("4"));
        frame.add(new JButton("5"));
        frame.add(new JButton("6"));

        frame.setVisible(true);
    }

}
