package interfacesGraficas;

import javax.swing.*;

public class EventoBoton {
    public static void main(String[] args) {

        JFrame ventana = new JFrame("Evento");
        ventana.setSize(275, 240); 
        ventana.setLayout(null);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton boton1 = new JButton("Haz click 1");
        boton1.setBounds(50, 20, 120, 30);
        
        JButton boton2 = new JButton("Haz click 2");
        boton2.setBounds(50, 60, 120, 30);

        JButton boton3 = new JButton("Haz click 3");
        boton3.setBounds(50, 100, 120, 30);

        JButton boton4 = new JButton("Haz click 4");
        boton4.setBounds(50, 140, 120, 30);

        JLabel etiqueta1 = new JLabel();
        etiqueta1.setBounds(180, 20, 150, 30);
        
        JLabel etiqueta2 = new JLabel();
        etiqueta2.setBounds(180, 60, 150, 30);
        
        JLabel etiqueta3 = new JLabel();
        etiqueta3.setBounds(180, 100, 150, 30);
        
        JLabel etiqueta4 = new JLabel();
        etiqueta4.setBounds(180, 140, 150, 30);

        
        boton1.addActionListener(e -> {
            etiqueta1.setText("¡Hola 1!");
            
            JOptionPane.showMessageDialog(ventana, "Has pulsado el botón 1", "Información", JOptionPane.INFORMATION_MESSAGE);
        }); 

        boton2.addActionListener(e -> {
        	 etiqueta2.setText("¡Hola 2!");
             
             JOptionPane.showMessageDialog(ventana, "Has pulsado el botón 2", "Saldo", JOptionPane.INFORMATION_MESSAGE);
         }); 
        
        boton3.addActionListener(e -> {
       	 etiqueta3.setText("¡Hola 3!");
            
            JOptionPane.showMessageDialog(ventana, "Has pulsado el botón 3", "Gestión", JOptionPane.INFORMATION_MESSAGE);
        }); 
       
        boton4.addActionListener(e -> {
       	 etiqueta4.setText("¡Hola 4!");
            
            JOptionPane.showMessageDialog(ventana, "Has pulsado el botón 4", "Consulta", JOptionPane.INFORMATION_MESSAGE);
        }); 
       
        ventana.add(boton1); ventana.add(etiqueta1);
        ventana.add(boton2); ventana.add(etiqueta2);
        ventana.add(boton3); ventana.add(etiqueta3);
        ventana.add(boton4); ventana.add(etiqueta4);

        ventana.setVisible(true);
    }
}