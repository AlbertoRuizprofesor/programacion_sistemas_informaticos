package calculadora;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;



public class MenuBasico extends JFrame {

    private JMenuBar mb = new JMenuBar();

    private JMenu menuArchivo,menuEdicion,menuHerra,menuAyuda;
    private JMenuItem itemAbrir, itemGuardar, itemCortar, itemCopiar, itemPegar;

    private ArrayList<JMenu> menus = new ArrayList<>();

    public MenuBasico() {

        setTitle("Ejemplo de Menú con JFrame");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);
        setJMenuBar(mb);

        // Crear menús principales
        menuArchivo = crearMenu(mb, "Archivo");
        menus.add(menuArchivo);

        menuEdicion=crearMenu(mb, "Edición");
        menus.add(menuEdicion);
        
        menuHerra=crearMenu(mb, "Herramientas");
        menus.add(menuHerra);
        menuAyuda=crearMenu(mb, "Ayuda");
        menus.add(menuAyuda);
        
        // Crear items dentro de Archivo
        itemAbrir = crearItem(menuArchivo, "Abrir");
        itemGuardar = crearItem(menuArchivo, "Guardar");
        itemCortar=crearItem(menuEdicion,"Cortar");
        itemCopiar=crearItem(menuEdicion,"Copiar");
        itemPegar=crearItem(menuEdicion,"Pegar");
        
        
        
        

        setBounds(10, 20, 300, 200);
        setLocationRelativeTo(null);
    }

    // Método para crear menú
    public static JMenu crearMenu(JMenuBar mb, String nombre) {
        JMenu menu = new JMenu(nombre);
        mb.add(menu);
        return menu;
    }

    // Método para crear item (sin listener)
    private JMenuItem crearItem(JMenu menu, String texto) {
        JMenuItem item = new JMenuItem(texto);
        menu.add(item);
        return item;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new MenuBasico().setVisible(true));
    }
}