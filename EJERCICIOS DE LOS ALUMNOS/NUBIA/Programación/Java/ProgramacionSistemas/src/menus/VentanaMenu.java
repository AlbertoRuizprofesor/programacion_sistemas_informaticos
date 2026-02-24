package menus;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.*;
 

public class VentanaMenu extends JFrame implements ActionListener {
	
    // Declaración de componentes del menú
    private JMenuBar mb = new JMenuBar(); // Barra de menú
    private JMenu menuArchivo,menuEdicion,menuHerra, menuAyuda;
    private JMenuItem itemAbrir, itemGuardar, itemCopiar, itemPegar, itemDibujar, itemColorear;
    private ArrayList<JMenu> menus=new ArrayList<>();
    
   
    public VentanaMenu() {
        setTitle("Ejemplo de Menú con JFrame"); // Establece el título de la ventana
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Define la operación de cierre de la ventana
        setLayout(null); // Layout nulo para posicionar manualmente los componentes
        setJMenuBar(mb); 
        	
        
        //creamos Archivo e items
        menuArchivo = new JMenu("Archivo"); 
        mb.add(menuArchivo);
        
        itemAbrir=new JMenuItem("Abrir");
        menuArchivo.add(itemAbrir);
        
        itemGuardar=new JMenuItem("Guardar");
        menuArchivo.add(itemGuardar);
        
        
        //creamos edicion e item
        menuEdicion = new JMenu("Edición"); 
        mb.add(menuEdicion);
        
        itemCopiar=new JMenuItem("Copiar");
        menuEdicion.add(itemCopiar);
        
        itemPegar=new JMenuItem("Pegar");
        menuEdicion.add(itemPegar);
        
        
        //creamos herramientas e item
        menuHerra = new JMenu("Herramientas"); 
        mb.add(menuHerra);
        itemDibujar=new JMenuItem("Dibujar");
        menuHerra.add(itemDibujar);
        itemColorear=new JMenuItem("Colorear");
        menuHerra.add(itemColorear);
        
        //JAVADOC
        //JUNIT
        
        
        
        // Configuración final de la ventana
        setBounds(10, 20, 300, 200); // Establece las dimensiones y la posición de la ventana
        setLocationRelativeTo(null); // Centra la ventana en la pantalla
    }
    
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() { // Asegura que la creación de la GUI se haga en el hilo de despacho de eventos
            public void run() {
               new VentanaMenu().setVisible(true); // Hace visible la ventana
            }
        });
    }


//actionPerfomed se usa cuando se va a clickar opciones d menus
    @Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
	}
}