package interfacesUnidad4;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import javax.swing.*;

public class Ejercicio2 {
public static void main (String[] args) {

		        JFrame ventana = new JFrame("Calculadora simple"); 
		        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
		        ventana.setSize(500, 400); 
		        ventana.setLayout(new BorderLayout()); 

		        JPanel norte = new JPanel(new FlowLayout()); 
		        norte.add(new JLabel("Operador 1:")); 
		        norte.add(new JTextField(10)); 
		        norte.add(new JLabel("Operador 2:")); 
		        norte.add(new JTextField(10));

		        JPanel centro = new JPanel(new GridLayout(2,2,20,20)); 
		        centro.add(new JButton("Sumar"));
		        centro.add(new JButton("Restar"));
		        centro.add(new JButton("Multiplicar"));
		        centro.add(new JButton("Dividir"));

		         
		        
		        JPanel  sur=new JPanel(new FlowLayout());
		        sur.add(new JLabel("Resultado:")); 
		        norte.add(new JTextField(10));
		        
		        ventana.add(norte, BorderLayout.NORTH); 
		        ventana.add(centro, BorderLayout.CENTER);
		        ventana.add(sur, BorderLayout.SOUTH);
		        ventana.setVisible(true); 

		    } 

		} 