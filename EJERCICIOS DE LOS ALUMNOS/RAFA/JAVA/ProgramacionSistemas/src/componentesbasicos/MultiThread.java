package componentesbasicos;


import javax.swing.*;
import java.awt.event.*;

public class MultiThread extends JFrame {

    private static final long serialVersionUID = 1L;
    private JComboBox<String> comboBox;  // Lenguajes
    private JComboBox<String> ide;        // IDEs
    private JLabel lblSeleccionaUnIde;

    public MultiThread() {
        // Configuración de la ventana
        setTitle("Ejemplo JComboBox con Threads");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setLayout(null);
        setSize(340, 150);

        // Label para lenguaje
        JLabel label = new JLabel("Selecciona un lenguaje:");
        label.setBounds(30, 6, 250, 30);
        getContentPane().add(label);

        // ComboBox de lenguajes
        String[] opcionesLenguaje = {"", "Java", "Kotlin", "PHP"};
        comboBox = new JComboBox<>(opcionesLenguaje);
        comboBox.setBounds(170, 11, 120, 20);
        getContentPane().add(comboBox);

        // Label para IDE
        lblSeleccionaUnIde = new JLabel("Selecciona un IDE:");
        lblSeleccionaUnIde.setBounds(30, 35, 250, 30);
        getContentPane().add(lblSeleccionaUnIde);

        // ComboBox de IDEs
        String[] opcionesIDE = {"", "Eclipse", "Visual Studio", "IntelliJ"};
        ide = new JComboBox<>(opcionesIDE);
        ide.setBounds(170, 40, 120, 20);
        getContentPane().add(ide);

        // Listener del combo de lenguajes
        comboBox.addActionListener(e -> {
            int selectedIndex = comboBox.getSelectedIndex();

            if (selectedIndex > 0) { // Ignorar opción vacía
                String lenguajeSeleccionado = opcionesLenguaje[selectedIndex];

                // Actualizar IDEs dependiendo del lenguaje
                SwingUtilities.invokeLater(() -> {
                    if (lenguajeSeleccionado.equals("Java")) {
                        ide.setModel(new DefaultComboBoxModel<>(new String[]{"", "Eclipse", "IntelliJ"}));
                    } else if (lenguajeSeleccionado.equals("Kotlin")) {
                        ide.setModel(new DefaultComboBoxModel<>(new String[]{"", "IntelliJ"}));
                    } else if (lenguajeSeleccionado.equals("PHP")) {
                        ide.setModel(new DefaultComboBoxModel<>(new String[]{"", "Visual Studio"}));
                    }
                });

                // Hilo para mostrar mensaje sin bloquear la ventana
                new Thread(() -> {
                    // Simular un proceso pesado
                    try {
                        Thread.sleep(500); // 0.5 segundos
                    } catch (InterruptedException ex) {
                        ex.printStackTrace();
                    }

                    // Mostrar mensaje en GUI
                    SwingUtilities.invokeLater(() -> {
                        JOptionPane.showMessageDialog(this,
                                "Has elegido el lenguaje: " + lenguajeSeleccionado,
                                "Lenguaje seleccionado",
                                JOptionPane.INFORMATION_MESSAGE);
                    });
                }).start();

                // Reiniciar selección del combo
                comboBox.setSelectedIndex(0);
            }
        });

        setVisible(true); // Hacer visible la ventana
    }

    // Método principal para ejecutar
    public static void main(String[] args) {
        new MultiThread();
    }
}