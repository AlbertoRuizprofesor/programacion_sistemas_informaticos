package interfacesUnidad1;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Ejercicio9 extends JFrame {
	public Ejercicio9() {
	        // Configuración de la ventana principal
	        setTitle("Matrix Choice");
	        setSize(300, 100);
	        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	        setLayout(new FlowLayout());
	        setLocationRelativeTo(null);

	        // Crear los RadioButtons
	        JRadioButton azul = new JRadioButton("Pastilla Azul");
	        JRadioButton roja = new JRadioButton("Pastilla roja");

	        // Agruparlos para que solo se pueda marcar uno a la vez
	        ButtonGroup grupo = new ButtonGroup();
	        grupo.add(azul);
	        grupo.add(roja);

	        // Añadir acción a la pastilla azul (la de la imagen)
	        azul.addActionListener(new ActionListener() {
	            @Override
	            public void actionPerformed(ActionEvent e) {
	                JOptionPane.showMessageDialog(null, 
	                    "Has elegida la opción azul, quédate en tu mundo de fantasía", 
	                    "Opción elegida", 
	                    JOptionPane.INFORMATION_MESSAGE);
	            }
	        });

	        // Añadir acción a la pastilla roja
	        roja.addActionListener(new ActionListener() {
	            @Override
	            public void actionPerformed(ActionEvent e) {
	                JOptionPane.showMessageDialog(null, 
	                    "Has elegido la pastilla roja, verás qué tan profundo llega el agujero", 
	                    "Opción elegida", 
	                    JOptionPane.WARNING_MESSAGE);
	            }
	        });

	        // Agregar componentes a la ventana
	        add(azul);
	        add(roja);
	    }

	    public static void main(String[] args) {
	        // Ejecutar la interfaz
	        SwingUtilities.invokeLater(() -> {
	            new Ejercicio9().setVisible(true);
	        });
	    }
	}
