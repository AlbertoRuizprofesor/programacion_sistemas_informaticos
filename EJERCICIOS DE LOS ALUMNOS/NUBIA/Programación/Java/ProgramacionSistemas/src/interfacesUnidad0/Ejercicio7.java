package interfacesUnidad0;

import javax.swing.*; 
import java.awt.*; 

public class Ejercicio7 {
	    public static void main(String[] args) { 

	        JFrame ventana = new JFrame("Layouts combinados"); 

	        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
	        ventana.setSize(500, 400); 
	        ventana.setLayout(new BorderLayout()); 

	        JPanel norte = new JPanel(new FlowLayout()); 

	        norte.add(new JButton("Botón 1")); 
	        norte.add(new JButton("Botón 2")); 

	        JPanel centro = new JPanel(new GridLayout(2,2)); 

	        centro.add(new JLabel("Nombre:")); 
	        centro.add(new JTextField(10)); 
	        centro.add(new JLabel("Edad:")); 
	        centro.add(new JTextField(3)); 
	        
	        JPanel  sur=new JPanel(new FlowLayout());
	        sur.add(new JButton("Botón 1"));
	        sur.add(new JButton("Botón 2"));
	        
	        ventana.add(norte, BorderLayout.NORTH); 
	        ventana.add(centro, BorderLayout.CENTER);
	        ventana.add(sur, BorderLayout.SOUTH);
	        ventana.setVisible(true); 

	    } 

	} 