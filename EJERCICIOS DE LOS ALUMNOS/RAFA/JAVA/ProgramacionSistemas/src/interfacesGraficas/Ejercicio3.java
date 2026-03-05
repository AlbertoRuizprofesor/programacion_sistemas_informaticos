package interfacesGraficas;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.*;

public class Ejercicio3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		JFrame frame = new JFrame("FlowLayout");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300,150);
		JPanel panel = new JPanel(new FlowLayout());
		panel.add(new JButton("Uno"));
        panel.add(new JButton("Dos"));
        panel.add(new JButton("Tres"));
        panel.add(new JButton("Cuatro"));
        panel.add(new JButton("cinco"));
        panel.add(new JButton("seis"));
        
        frame.setLocationRelativeTo(null);
        frame.add(panel);
        frame.setVisible(true);
    }
}



