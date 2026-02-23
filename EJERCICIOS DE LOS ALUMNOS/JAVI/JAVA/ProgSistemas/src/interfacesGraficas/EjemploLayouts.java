package interfacesGraficas;

import javax.swing.*;
import java.awt.*;

public class EjemploLayouts {
    public static void main(String[] args) {
        JFrame ventana = new JFrame("Layouts combinados");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setSize(500, 400);
        ventana.setLayout(new BorderLayout());

        JPanel norte = new JPanel(new FlowLayout());
        norte.add(new JButton("Botón 1"));
        norte.add(new JButton("Botón 2"));
        norte.add(new JButton("Botón 3"));
        norte.add(new JButton("Botón 4"));

        JPanel centro = new JPanel(new GridLayout(4,4));
        centro.add(new JLabel("Nombre:"));
        centro.add(new JTextField(10));
        centro.add(new JLabel("Edad:"));
        centro.add(new JTextField(3));
        centro.add(new JLabel("Asignatura:"));
        centro.add(new JTextField(20));
        centro.add(new JLabel("Nota:"));
        centro.add(new JTextField(3));
        
        JPanel sur = new JPanel(new FlowLayout());
        sur.add(new JButton("Enviar"));
        sur.add(new JButton("Cancelar"));

        ventana.add(norte, BorderLayout.NORTH);
        ventana.add(centro, BorderLayout.CENTER);
        ventana.add(sur, BorderLayout.SOUTH);

        ventana.setVisible(true);
    }
}
