package interfacesGraficas;

import javax.swing.*;

public class ExampleInvoke extends JFrame {

    public ExampleInvoke() {
        setTitle("Ventana segura");
        setSize(300,150);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        add(new JButton("Hola"));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() ->
            new ExampleInvoke().setVisible(true)
        );
    }
}



