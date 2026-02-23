package interfacesGraficas;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Ventana8Menu extends JFrame implements ActionListener {
	// Declaración de componentes del menú
	private JMenuBar mb = new JMenuBar(); // Barra de menú
	private JMenu menuClientes, menuProveedores, menuProductos; // Menús para clientes y proveedores
	private JMenuItem mi1; // Elemento de menú "Abrir"

	public Ventana8Menu() {
		setTitle("Ejemplo de Menú con JFrame"); // Establece el título de la ventana
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Define la operación de cierre de la ventana
		setLayout(null); // Layout nulo para posicionar manualmente los componentes

		setJMenuBar(mb); // Asigna la barra de menú al JFrame

		// Configuración del menú "Clientes"
		menuClientes = new JMenu("Clientes"); // Instancia del menú "Clientes"
		mb.add(menuClientes); // Añade el menú "Clientes" a la barra de menú

		mi1 = new JMenuItem("Abrir"); // Crea un elemento de menú "Abrir"
		mi1.addActionListener(this); // Añade un ActionListener para manejar eventos cuando se selecciona este ítem
		menuClientes.add(mi1); // Añade el ítem "Abrir" al menú "Clientes"

		JMenuItem mi2 = new JMenuItem("Guardar"); // Crea otro elemento de menú "Guardar"
		mi2.addActionListener(this); // Añade un ActionListener para manejar eventos cuando se selecciona este ítem
		menuClientes.add(mi2); // Añade el ítem "Guardar" al menú "Clientes"
		
		JMenuItem mi3 = new JMenuItem("Guardar como"); // Crea otro elemento de menú "Guardar"
		mi3.addActionListener(this); // Añade un ActionListener para manejar eventos cuando se selecciona este ítem
		menuClientes.add(mi3); // Añade el ítem "Guardar" al menú "Clientes"


		// Configuración del menú "Proveedores"
		menuProveedores = new JMenu("Proveedores"); // Instancia del menú "Proveedores"
		mb.add(menuProveedores); // Añade el menú "Proveedores" a la barra de menú
		
		menuProductos = new JMenu("Productos");
		mb.add(menuProductos);
		

		// Configuración final de la ventana
		setBounds(10, 20, 300, 200); // Establece las dimensiones y la posición de la ventana
		setLocationRelativeTo(null); // Centra la ventana en la pantalla
	}

	// Método que maneja los eventos de los elementos del menú
	public void actionPerformed(ActionEvent e) {
		Container contentPane = getContentPane(); // Obtiene el panel de contenido de la ventana
		if (e.getSource() == mi1) { // Comprueba si el evento proviene del ítem "Abrir"
			contentPane.setBackground(new Color(255, 0, 0)); // Cambia el color de fondo a rojo si se selecciona "Abrir"
		}
	}

	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Runnable() { // Asegura que la creación de la GUI se haga en el hilo de despacho
													// de eventos
			public void run() {
				Ventana8Menu formulario1 = new Ventana8Menu(); // Crea una instancia de la ventana
				formulario1.setVisible(true); // Hace visible la ventana
			}
		});
	}
}
