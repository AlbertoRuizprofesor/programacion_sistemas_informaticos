package interfacesUnidad1;

import javax.swing.*; // Importa las clases necesarias para crear la interfaz gráfica de usuario (GUI).

public class Ejercicio1 extends JFrame {


	public Ejercicio1() {

	setTitle("Ejemplo JTextField"); // Establece el título de la ventana.

	setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Define la operación de cierre de la ventana. Aquí, el programa se cerrará al cerrar la ventana.

	setLayout(null); // Establece un layout nulo, lo que significa que los componentes deben posicionarse manualmente.

	setSize(300, 100); // Define el tamaño de la ventana (ancho y alto en píxeles).


	// Crea un JLabel con el texto "Indica tu nombre:"

	JLabel label = new JLabel("Indica tu nombre:");

	label.setBounds(10, 10, 150, 20); // Establece la posición (x, y) y el tamaño (ancho, alto) del JLabel.

	add(label); // Añade el JLabel a la ventana.


	// Crea un JTextField para que el usuario pueda introducir su nombre.

	JTextField textField = new JTextField();

	textField.setBounds(160, 10, 120, 20); // Establece la posición (x, y) y el tamaño (ancho, alto) del JTextField.

	add(textField); // Añade el JTextField a la ventana.


	setLocationRelativeTo(null); // Centra la ventana en la pantalla.

	}


	public static void main(String[] args) {

	// Este es el punto de entrada del programa. Utiliza SwingUtilities.invokeLater para asegurarse de que la creación y manipulación de la GUI se realicen en el hilo de despacho de eventos de Swing.

	SwingUtilities.invokeLater(() -> {

	new Ejercicio1().setVisible(true); // Crea una instancia de la ventana y la hace visible.

	});
	}
}