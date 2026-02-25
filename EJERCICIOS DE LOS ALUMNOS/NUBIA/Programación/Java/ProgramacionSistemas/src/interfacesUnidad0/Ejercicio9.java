package interfacesUnidad0;

import javax.swing.*; 
import java.awt.event.*; 

public class Ejercicio9 {
	    public static void main(String[] args) { 

	        JFrame ventana = new JFrame("Evento teclado"); 
	        ventana.setSize(300, 200); 
	        ventana.setLayout(null); 
	        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 

	        JTextField campo = new JTextField(); 
	        campo.setBounds(50, 50, 200, 30); 

	        JLabel etiqueta = new JLabel(); 
	        etiqueta.setBounds(50, 100, 200, 30); 

	 
	        campo.addKeyListener(new KeyAdapter() { 
	        	public void keyPressed(KeyEvent e) { 
	                etiqueta.setText("Tecla: " + e.getKeyChar()); 
	            } 
	        }); 

	 
	        ventana.add(campo); 
	        ventana.add(etiqueta); 
	        ventana.setVisible(true); 
	    } 

	} 