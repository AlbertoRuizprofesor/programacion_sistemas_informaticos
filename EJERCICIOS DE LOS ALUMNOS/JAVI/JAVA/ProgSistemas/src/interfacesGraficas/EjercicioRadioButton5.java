package interfacesGraficas;

import javax.swing.*;
import java.awt.FlowLayout; // Importante para definir cómo se alinean los elementos

public class EjercicioRadioButton5 extends JFrame {
    public EjercicioRadioButton5() {
        setTitle("Ejemplo JRadioButton");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // 1. Crear los RadioButtons
        JRadioButton radioButton1 = new JRadioButton("Opción 1", true); // "true" para que aparezca seleccionado
        JRadioButton radioButton2 = new JRadioButton("Opción 2");
        JRadioButton radioButton3 = new JRadioButton("Opción 3");
        JRadioButton radioButton4 = new JRadioButton("Opción 4");
        JRadioButton radioButton5 = new JRadioButton("Opción 5");
          
        // 2. Agruparlos (Lógica de exclusión mutua)
        ButtonGroup group = new ButtonGroup();
        group.add(radioButton1);
        group.add(radioButton2);
        group.add(radioButton3);
        group.add(radioButton4);
        group.add(radioButton5);
        
        // 3. Crear el panel y añadir los componentes (Interfaz visual)
        JPanel panel = new JPanel();
        panel.add(radioButton1);
        panel.add(radioButton2);
        panel.add(radioButton3);
        panel.add(radioButton4);
        panel.add(radioButton5);
        
        // 4. Configuración final de la ventana
        add(panel); // getContentPane().add(panel) también es válido, pero add() es más directo hoy en día
        pack(); 
        setLocationRelativeTo(null); // Centra la ventana en pantalla
    }

    public static void main(String[] args) {
        // Uso de Lambda para el hilo de despacho de eventos
        SwingUtilities.invokeLater(() -> {
            new EjercicioRadioButton5().setVisible(true);
        });
    }
}

