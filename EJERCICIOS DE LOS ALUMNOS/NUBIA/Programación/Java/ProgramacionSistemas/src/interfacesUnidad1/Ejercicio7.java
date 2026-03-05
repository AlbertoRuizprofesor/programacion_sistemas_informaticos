package interfacesUnidad1; 

import javax.swing.*; 
import java.awt.*; 

public class Ejercicio7 extends JFrame { // La clase extiende JFrame para crear una ventana. 

    public Ejercicio7() { 

        setTitle("Formulario Básico"); // Establece el título de la ventana. 
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Define la operación de cierre de la ventana. Aquí, el programa se cerrará al cerrar la ventana. 
        setLayout(new GridLayout(4, 2)); // Establece un GridLayout con 4 filas y 2 columnas para organizar los componentes. 


        // Crea un JLabel con el texto "Comentario:" 

        JLabel labelComentario = new JLabel("Comentario:"); 

         

        // Crea un JTextArea para que el usuario pueda ingresar un comentario. 

        JTextArea textAreaComentario = new JTextArea(); 

        textAreaComentario.setLineWrap(true); // Permite que las líneas se ajusten al ancho del JTextArea. 

        textAreaComentario.setWrapStyleWord(true); // Asegura que las líneas se ajusten por palabra, no por carácter. 

         

        // Añade un JScrollPane para permitir el desplazamiento si el contenido del JTextArea es demasiado grande. 

        JScrollPane scrollPane = new JScrollPane(textAreaComentario); 

         

        // Añade el JLabel y el JScrollPane (que contiene el JTextArea) al formulario. 

        add(labelComentario); 

        add(scrollPane); 

 

        // Crea un botón "Enviar" con un ActionListener para manejar la acción cuando el botón es presionado. 

        JButton botonEnviar = new JButton("Enviar"); 

        botonEnviar.addActionListener(e -> { 

            // Aquí puedes agregar la lógica para procesar la información del formulario. 

            String comentario = textAreaComentario.getText(); // Obtiene el texto del JTextArea. 

 

            // Ejemplo de imprimir la información en la consola. 

            System.out.println("Comentario: " + comentario); 

        }); 

        add(botonEnviar); // Añade el botón al formulario. 

 

        pack(); // Ajusta el tamaño de la ventana para que se adapte a los componentes que contiene. 

        setLocationRelativeTo(null); // Centra la ventana en la pantalla. 

    } 

 

    public static void main(String[] args) { 

        // Este es el punto de entrada del programa. Utiliza SwingUtilities.invokeLater para asegurarse de que la creación y manipulación de la GUI se realicen en el hilo de despacho de eventos de Swing. 

        SwingUtilities.invokeLater(() -> { 

            new Ejercicio7().setVisible(true); // Crea una instancia de la ventana y la hace visible. 

        }); 

    } 

} 