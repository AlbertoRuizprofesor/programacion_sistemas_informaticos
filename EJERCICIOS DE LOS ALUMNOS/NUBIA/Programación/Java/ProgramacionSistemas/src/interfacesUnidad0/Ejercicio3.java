package interfacesUnidad0;

import javax.swing.*; 
import java.awt.*;

public class Ejercicio3 {
    public static void main(String[] args) { 

        JFrame frame = new JFrame("FlowLayout"); 

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        frame.setSize(300, 150); 

 

        JPanel panel = new JPanel(new FlowLayout()); 

        panel.add(new JButton("Uno")); 
        panel.add(new JButton("Dos"));
        panel.add(new JButton("Tres")); 
        panel.add(new JButton("Cuatro")); 

        frame.add(panel); 
        frame.setVisible(true);
    }
}
