package menus;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Ventana8Menu extends JFrame implements ActionListener {
    // Declaración de componentes del menú
    private JMenuBar mb = new JMenuBar(); // Barra de menú
    private JMenu archivos; // Menús para clientes y proveedores
    private JMenuItem mi1,mi2; // Elemento de menú "Abrir"

    public Ventana8Menu() {
        setTitle("Ejemplo de Menú con JFrame"); // Establece el título de la ventana
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Define la operación de cierre de la ventana
        setLayout(null); // Layout nulo para posicionar manualmente los componentes

        setJMenuBar(mb); // Asigna la barra de menú al JFrame
        // Configuración del menú "Clientes"
        archivos = new JMenu("Archivos"); // Instancia del menú "Clientes"
        mb.add(archivos); // Añade el menú "Clientes" a la barra de menú

        mi1 = new JMenuItem("Abrir"); // Crea un elemento de menú "Abrir"
        mi1.addActionListener(this); // Añade un ActionListener para manejar eventos cuando se selecciona este ítem
        archivos.add(mi1); // Añade el ítem "Abrir" al menú "Clientes"

        mi2 = new JMenuItem("Guardar"); // Crea otro elemento de menú "Guardar"
        mi2.addActionListener(this); // Añade un ActionListener para manejar eventos cuando se selecciona este ítem
        archivos.add(mi2); // Añade el ítem "Guardar" al menú "Clientes"
        
        // Configuración final de la ventana
        setBounds(10, 20, 300, 200); // Establece las dimensiones y la posición de la ventana
        setLocationRelativeTo(null); // Centra la ventana en la pantalla
    }

    // Método que maneja los eventos de los elementos del menú
    public void actionPerformed(ActionEvent e) {
        Container contentPane = getContentPane(); // Obtiene el panel de contenido de la ventana
        if (e.getSource() == mi1) { // Comprueba si el evento proviene del ítem "Abrir"
            contentPane.setBackground(new Color(255, 0, 160)); // Cambia el color de fondo a rojo si se selecciona "Abrir"
        }
        else {
        	 contentPane.setBackground(new Color(25, 10, 10)); 
        }   
    }
    public void crearItem(JMenuItem item, JMenu menu,String text) {
    	 item=new JMenuItem(text);
         item.addActionListener(this);
         menu.add(item);
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() { // Asegura que la creación de la GUI se haga en el hilo de despacho de eventos
            public void run() {
               new Ventana8Menu().setVisible(true); // Hace visible la ventana
            }
        });
    }
}