package interfacesGraficas;

import javax.swing.*;
import java.awt.event.*;

public class EjemploWindowListener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Ejemplo WindowListener");

        // 1. IMPORTANTE: Cambiamos el comportamiento por defecto
        // DO_NOTHING_ON_CLOSE permite que nuestro WindowListener tome el control total
        frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);

        // 2. Registrar el escuchador usando WindowAdapter
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.out.println("Ventana cerrándose... liberando recursos.");
                // Aquí podrías guardar datos antes de salir
                System.exit(0); 
            }
        });

        frame.setSize(300, 200);
        // 3. Centrar la ventana (opcional pero recomendado)
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}