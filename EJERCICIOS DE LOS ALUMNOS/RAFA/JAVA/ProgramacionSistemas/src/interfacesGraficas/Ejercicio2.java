package interfacesGraficas;
import javax.swing.*;

@SuppressWarnings("serial")
public class Ejercicio2 extends JFrame {

    public Ejercicio2() {
        super("Mi Ventana");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Ejercicio2();
    }
}
