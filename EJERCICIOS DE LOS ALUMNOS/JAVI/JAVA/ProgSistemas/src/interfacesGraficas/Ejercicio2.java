package interfacesGraficas;

import javax.swing.*;

public class Ejercicio2 extends JFrame {

    public Ejercicio2() {
        super("Mi Ventana2");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Ejercicio2();
    }
}
