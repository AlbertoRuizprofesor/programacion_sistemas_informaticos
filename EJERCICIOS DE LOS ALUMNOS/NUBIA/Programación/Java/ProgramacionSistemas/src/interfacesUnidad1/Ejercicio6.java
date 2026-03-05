package interfacesUnidad1;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Ejercicio6 extends JFrame {

    private JCheckBox chkTerminos, chkPublicidad;

    public Ejercicio6() {
        // 1. Configuración de la ventana
        setTitle("Ejemplo JCheckBox");
        setSize(500, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Usamos FlowLayout para que los elementos se pongan uno al lado del otro
        setLayout(new FlowLayout(FlowLayout.LEFT, 20, 50));

        // 2. Creación de los CheckBoxes
        chkTerminos = new JCheckBox("Aceptar términos y condiciones");
        chkPublicidad = new JCheckBox("Desea recibir publicidad");

        // 3. Añadir los componentes a la ventana
        add(chkTerminos);
        add(chkPublicidad);

        // 4. Evento: ¿Qué pasa cuando haces clic?
        chkTerminos.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Si la casilla está seleccionada, muestra el mensaje
                if (chkTerminos.isSelected()) {
                    JOptionPane.showMessageDialog(null, 
                        "Has aceptado los términos y condiciones.", 
                        "Indica el código", 
                        JOptionPane.INFORMATION_MESSAGE);
                }
            }
        });
    }

    public static void main(String[] args) {
        new Ejercicio6().setVisible(true);
    }
}