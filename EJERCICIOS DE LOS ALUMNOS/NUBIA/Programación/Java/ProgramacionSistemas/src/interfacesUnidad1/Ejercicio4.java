package interfacesUnidad1;

import javax.swing.*; // Importa las clases necesarias para la GUI.
import java.awt.event.ActionEvent; // Importa la clase ActionEvent para manejar eventos de acciones.
import java.awt.event.ActionListener; // Importa la interfaz ActionListener para manejar eventos de acciones.


public class Ejercicio4 extends JFrame { // La clase extiende JFrame para crear una ventana.

private JComboBox<String> comboBox; // Declara un JComboBox que contendrá una lista desplegable de opciones.


public Ejercicio4() {

setTitle("Ejemplo JComboBox"); // Establece el título de la ventana.

setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Define la operación de cierre de la ventana. Aquí, el programa se cerrará al cerrar la ventana.

setLayout(null); // Establece un layout nulo para posicionar los componentes manualmente.

setSize(300, 100); // Define el tamaño de la ventana.


// Crea un JLabel con el texto "Selecciona un lenguaje:"

JLabel label = new JLabel("Selecciona un lenguaje:");

label.setBounds(10, 10, 150, 20); // Posiciona y establece el tamaño del JLabel.

add(label); // Añade el JLabel a la ventana.


//Crea un JLabel con el texto "Selecciona un IDE:"

JLabel label1 = new JLabel("Selecciona un IDE:");

label1.setBounds(80, 10, 150, 20); // Posiciona y establece el tamaño del JLabel.

add(label1); // Añade el JLabel a la ventana.


// Define un array de strings con las opciones que se mostrarán en el JComboBox.

String[] opciones = {"Python", "Java", "JAVASCRIPT"};

comboBox = new JComboBox<>(opciones); // Crea el JComboBox con las opciones definidas.

comboBox.setBounds(160, 10, 120, 20); // Posiciona y establece el tamaño del JComboBox.

add(comboBox); // Añade el JComboBox a la ventana.


// Añade un ActionListener al JComboBox para manejar la selección de opciones.

comboBox.addActionListener(new ActionListener() {

public void actionPerformed(ActionEvent e) {

int selectedIndex = comboBox.getSelectedIndex(); // Obtiene el índice de la opción seleccionada.

System.out.println(selectedIndex); // Imprime el índice de la opción seleccionada en la consola.


String seleccion = opciones[selectedIndex]; // Obtiene el valor de la opción seleccionada.

mostrarMensaje("Indica el código", "Has elegido: " + seleccion); // Muestra un mensaje con la opción seleccionada.

}

});


setLocationRelativeTo(null); // Centra la ventana en la pantalla.

}


// Método para mostrar un cuadro de diálogo con un mensaje.

private void mostrarMensaje(String titulo, String mensaje) {

JOptionPane.showMessageDialog(this, mensaje, titulo, JOptionPane.INFORMATION_MESSAGE);

}


public static void main(String[] args) {

// Punto de entrada del programa. Utiliza SwingUtilities.invokeLater para asegurar que la GUI se maneje en el hilo de despacho de eventos de Swing.

SwingUtilities.invokeLater(() -> {

new Ejercicio3().setVisible(true); // Crea una instancia de la ventana y la hace visible.

});

}
}