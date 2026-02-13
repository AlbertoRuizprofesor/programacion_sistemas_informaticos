package joptionpane;

import javax.swing.JOptionPane;

public class ShowInputDialogExample {
	public static void main(String[] args) {
		String name=JOptionPane.showInputDialog("Escribe tu nombre: ");
		JOptionPane.showMessageDialog(null, "Hola, "+name);
		
		
	}

}
