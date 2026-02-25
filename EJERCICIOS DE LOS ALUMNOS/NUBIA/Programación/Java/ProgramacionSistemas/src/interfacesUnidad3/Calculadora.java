package interfacesUnidad3;
import javax.swing.*;
import java.awt.*;

public class Calculadora extends JFrame {

    public Calculadora() {
        setTitle("Calculadora");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(350, 450);
        setLocationRelativeTo(null);
        
        // Panel principal con GridBagLayout
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();
        c.fill = GridBagConstraints.BOTH; // Expandir en ambas direcciones
        c.insets = new Insets(2, 2, 2, 2); // Espaciado entre botones
        c.weightx = 1.0;
        c.weighty = 1.0;

        // 1. Pantalla (Ocupa toda la fila superior)
        JTextField pantalla = new JTextField("0");
        pantalla.setHorizontalAlignment(JTextField.RIGHT);
        pantalla.setFont(new Font("Arial", Font.PLAIN, 28));
        c.gridx = 0; c.gridy = 0;
        c.gridwidth = 4; // Ocupa 4 columnas
        panel.add(pantalla, c);

        // --- FILA 1 ---
        c.gridwidth = 1; // Reset a 1 columna
        agregarBoton("/", 0, 1, panel, c);
        agregarBoton("*", 1, 1, panel, c);
        agregarBoton("-", 2, 1, panel, c);
        agregarBoton("C", 3, 1, panel, c);

        // --- FILA 2 ---
        agregarBoton("9", 0, 2, panel, c);
        agregarBoton("8", 1, 2, panel, c);
        agregarBoton("7", 2, 2, panel, c);
        
        // Botón "+" (Ocupa 2 filas de alto)
        c.gridx = 3; c.gridy = 2;
        c.gridheight = 2; 
        panel.add(new JButton("+"), c);

        // --- FILA 3 ---
        c.gridheight = 1; // Reset a 1 fila
        agregarBoton("6", 0, 3, panel, c);
        agregarBoton("5", 1, 3, panel, c);
        agregarBoton("4", 2, 3, panel, c);

        // --- FILA 4 ---
        agregarBoton("3", 0, 4, panel, c);
        agregarBoton("2", 1, 4, panel, c);
        agregarBoton("1", 2, 4, panel, c);

        // Botón "=" (2 filas)
        c.gridx = 3; c.gridy = 4;
        c.gridheight = 2;
        panel.add(new JButton("="), c);

        // --- FILA 5 ---
        // Botón "0" (2 columnas)
        c.gridx = 0; c.gridy = 5;
        c.gridwidth = 2;
        c.gridheight = 1;
        panel.add(new JButton("0"), c);

        // Botón "."
        c.gridx = 2; c.gridy = 5;
        c.gridwidth = 1;
        agregarBoton(".", 2, 5, panel, c);

        add(panel);
    }

    // Método auxiliar para no repetir código
    private void agregarBoton(String texto, int x, int y, JPanel p, GridBagConstraints c) {
        JButton b = new JButton(texto);
        c.gridx = x;
        c.gridy = y;
        p.add(b, c);
    }

    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {}
        
        SwingUtilities.invokeLater(() -> new Calculadora().setVisible(true));
    }
}