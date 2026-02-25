package componentesbasicos;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class EjercicioRadioButton6 extends JFrame {
    public EjercicioRadioButton6() {
        setTitle("Matrix");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JRadioButton radioButton1 = new JRadioButton("Pastilla Azul");
        JRadioButton radioButton2 = new JRadioButton("Pastilla roja");
        JRadioButton radioButton3 = new JRadioButton("Pastilla Verde");
        JRadioButton radioButton4 = new JRadioButton("Pastilla Morada");
      
        ButtonGroup group = new ButtonGroup();
        group.add(radioButton1);
        group.add(radioButton2);
        group.add(radioButton3);
        group.add(radioButton4);

        JPanel panel = new JPanel();
        panel.add(radioButton1);
        panel.add(radioButton2);
        panel.add(radioButton3);
        panel.add(radioButton4);
        add(panel);

        pack();
        setLocationRelativeTo(null);
        //
        radioButton1.addActionListener(e -> 
        mostrarMensaje("Eleccion elegida", 
        "Has elegida la opcion azul, quedate en tu mundo de fantasia")
    );
      
        radioButton2.addActionListener(e -> 
        mostrarMensaje("Eleccion elegida", 
        "Has elegido la opción roja, te contaré la verdad sobre Matrix.")
    );
    
        radioButton3.addActionListener(e -> 
        mostrarMensaje("Eleccion elegida", 
        "Has elegida la opcion verde, comete una manzana")
    );
      
        radioButton4.addActionListener(e -> 
        mostrarMensaje("Eleccion elegida", 
        "Has elegido la opción morada, la lengua te ha cambiado de color.")
    );    
      
}
    private void mostrarMensaje(String titulo, String mensaje) {
        JOptionPane.showMessageDialog(this, mensaje, titulo, JOptionPane.INFORMATION_MESSAGE);
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new EjercicioRadioButton6().setVisible(true);
        });
    }
}
