package menus;

import java.awt.EventQueue;
import javax.swing.*;

public class VentanaMenu extends JFrame {

    private static final long serialVersionUID = 1L;
    private JPanel contentPane;

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
                VentanaMenu frame = new VentanaMenu();
                frame.setVisible(true);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    public VentanaMenu() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 450, 300);

        contentPane = new JPanel();
        setContentPane(contentPane);

        // --- Barra de menú ---
        JMenuBar barraMenu = new JMenuBar();
        setJMenuBar(barraMenu); // 🔥 IMPORTANTE

        // --- Menú ---
        JMenu menuClientes = new JMenu("Clientes");
        barraMenu.add(menuClientes);

        // --- Opciones del menú ---
        JMenuItem itemNuevo = new JMenuItem("Nuevo");
        JMenuItem itemEliminar = new JMenuItem("Eliminar");
        JMenuItem itemCargar = new JMenuItem("cargar");
        

        menuClientes.add(itemNuevo);
        menuClientes.add(itemEliminar);
        menuClientes.add(itemCargar);

        // --- Eventos ---
        itemNuevo.addActionListener(e -> 
            JOptionPane.showMessageDialog(this, "Nuevo cliente")
        );

        itemEliminar.addActionListener(e -> 
            JOptionPane.showMessageDialog(this, "Eliminar cliente")
        );
        
        itemCargar.addActionListener(e -> 
        JOptionPane.showMessageDialog(this, "cargar cliente")
    );
    }
}