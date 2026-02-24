package interfacesUnidad4;

import java.awt.FlowLayout; 
import java.awt.event.ActionEvent; 
import java.awt.event.ActionListener; 
import javax.swing.*; 

public class Ejercicio1 extends JFrame{ 
	public Ejercicio1() { 
		setTitle("Mi ventana"); 

        setSize(300, 200); 

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 

        JButton button = new JButton("Clica aquí"); 

       //configuramos un FlowLayout 

        setLayout(new FlowLayout()); 

        add(button); 

        // Agregar un ActionListener al botón 

        button.addActionListener(new ActionListener() { 

             

@Override 

public void actionPerformed(ActionEvent e) { 

 System.out.println("Botón clickeado"); 

 

} 

        }); 

} 

 

    public static void main(String[] args) { 

    	    //// Ejecutar la GUI en el hilo de despacho de eventos 

 

        SwingUtilities.invokeLater(() -> { 

        	 

            new Ejercicio1().setVisible(true); 

        }); 

         

    } 

    
} 

