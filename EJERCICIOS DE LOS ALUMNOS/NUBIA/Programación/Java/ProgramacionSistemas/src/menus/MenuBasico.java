package menus;

import javax.swing.*;
import java.util.ArrayList;

public class MenuBasico extends JFrame {

    private JMenuBar mb = new JMenuBar();

    // Nombres de menús
    private String[] menus = {"Archivo", "Edición", "Herramientas", "Ayuda"};

    // Lista de menús creados (para acceder por índice)
    private ArrayList<JMenu> menusCreados = new ArrayList<>(); //archivo, ediciom etc, array de objetos, tipo jmenu
    
    private String[] itemsArchivo = {"Abrir", "Guardar", "Salir"};
    private String[] itemsEdicion = {"Cortar", "Copiar", "Pegar"};
    private String[] itemsHerra = {"Javadoc", "Extensiones"};
    private String[] itemsAyuda = {"PDF", "Web"};

    public MenuBasico() {
        setTitle("Ejemplo Menús + Items con Lambda");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);
        setJMenuBar(mb);

        // 1) Crear menús
        crearMenus(menus); //creamos los menus usando el array

        // 2) Items para cada menú (arrays)
        

        // 3) Crear items en cada menú con un solo método, 
        crearItems(menusCreados.get(0), itemsArchivo); // Archivo
        crearItems(menusCreados.get(1), itemsEdicion); // Edición
        crearItems(menusCreados.get(2), itemsHerra);
        crearItems(menusCreados.get(3), itemsAyuda);
        
        

        setBounds(10, 20, 400, 250);
        setLocationRelativeTo(null);
    }

    // Crea todos los menús a partir del array de nombres
    private void crearMenus(String[] nombres) {
        for (String nomb : nombres) {
            JMenu menu = new JMenu(nomb);
            mb.add(menu);
            menusCreados.add(menu); //los añadimos al array menus creados
        }
    }

    // Crea todos los items de un menú desde un array + listener lambda
    private void crearItems(JMenu menu, String[] nombresItems) {
        for (String nombreItem : nombresItems) {
            JMenuItem item = new JMenuItem(nombreItem);

            // ✅ Lambda: al pulsar, muestra qué has pulsado
            item.addActionListener(e ->
                    JOptionPane.showMessageDialog(
                            this,
                            "Has pulsado \"" + nombreItem + "\""
                    )
            );

            menu.add(item);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new MenuBasico().setVisible(true));
    }
}