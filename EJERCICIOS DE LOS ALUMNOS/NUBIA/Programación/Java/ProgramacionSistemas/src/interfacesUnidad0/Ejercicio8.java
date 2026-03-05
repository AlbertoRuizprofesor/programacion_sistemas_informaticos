package interfacesUnidad0;

import javax.swing.*; 

public class Ejercicio8 extends JFrame {
	    public static void main(String[] args) { 

	        JFrame ventana = new JFrame("Evento"); 
	        ventana.setSize(400, 200); 
	        ventana.setLayout(null); 
	        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 

	        JButton boton = new JButton("Haz clic"); 
	        boton.setBounds(50, 50, 150, 30); 
	        
	        JButton boton1=new JButton("NO hagas clic");
	        boton1.setBounds(200,50,150,30);
	        

	        JLabel etiqueta = new JLabel(); 
	        etiqueta.setBounds(50, 100, 200, 30); 
	        
	        JLabel etiqueta1=new JLabel();
	        etiqueta1.setBounds(200, 100, 200, 30);
	        
	        boton.addActionListener(e -> etiqueta.setText("¡Botón clicado!")); 
	        boton1.addActionListener(e -> etiqueta1.setText("No haces caso eh..."));
	       
	        ventana.add(boton); 
	        ventana.add(etiqueta); 
	        
	        ventana.add(boton1);
	        ventana.add(etiqueta1);
	        
	        ventana.setVisible(true); 
	    }
}