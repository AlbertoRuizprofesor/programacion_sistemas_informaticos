package interfacesGraficas;

import javax.swing.*;

public class Ejercicio8 {
    public static void main(String[] args) {

        JFrame ventana = new JFrame("Ventana 1");
        ventana.setSize(400, 200);
        ventana.setLayout(null);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        

        JButton boton = new JButton("Haz clic");
        boton.setBounds(50, 50, 150, 30);

        JButton boton2 = new JButton("Haz clic otra vez");
        boton2.setBounds(200, 50, 150, 30);

        JLabel etiqueta = new JLabel();
        etiqueta.setBounds(50, 100, 200, 30);

        JLabel etiqueta2 = new JLabel();
        etiqueta2.setBounds(200, 100, 200, 30);

        boton.addActionListener(e -> etiqueta.setText("¡Botón clicado!"));
        boton2.addActionListener(e -> etiqueta2.setText("¡Botón clicado otra vez!"));

        ventana.add(boton);
        ventana.add(etiqueta);

        ventana.add(boton2);
        ventana.add(etiqueta2);

        ventana.setVisible(true);
        
    }
}
