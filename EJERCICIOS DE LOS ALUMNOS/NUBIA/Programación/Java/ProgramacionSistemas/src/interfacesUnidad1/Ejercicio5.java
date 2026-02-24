package interfacesUnidad1;

import javax.swing.*; // Importa las clases necesarias para crear la interfaz gráfica de usuario (GUI).

public class Ejercicio5 extends JFrame {

	public Ejercicio5() {

	setTitle("Ejemplo JCheckBox"); // Establece el título de la ventana.

	setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Define la operación de cierre de la ventana. Aquí, el programa se cerrará al cerrar la ventana.


	// Crea un JCheckBox con el texto "Aceptar términos y condiciones"

	JCheckBox checkBox = new JCheckBox("Aceptar términos y condiciones");

	add(checkBox); // Añade el JCheckBox a la ventana.


	setSize(300, 200); // Define el tamaño de la ventana (ancho y alto en píxeles).

	setLocationRelativeTo(null); // Centra la ventana en la pantalla.

	}


	public static void main(String[] args) {

	// Este es el punto de entrada del programa. Utiliza SwingUtilities.invokeLater para asegurarse de que la creación y manipulación de la GUI se realicen en el hilo de despacho de eventos de Swing.

	SwingUtilities.invokeLater(() -> {

	new Ejercicio5().setVisible(true); // Crea una instancia de la ventana y la hace visible.

	});

	}


}
