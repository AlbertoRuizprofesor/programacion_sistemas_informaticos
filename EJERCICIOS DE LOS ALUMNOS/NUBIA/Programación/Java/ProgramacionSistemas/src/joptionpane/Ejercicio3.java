package joptionpane;

import javax.swing.JOptionPane;

public class Ejercicio3 {
	public static void main (String[] args) {
		
		String [] options = {"Piedra", "Papel", "Tijeras", "Spock" };
		
		var selection = JOptionPane.showOptionDialog(null,  "Selecciona una: ",  "¡a jugar!", 0, 3, null, options, options[0]);
		
		if (selection == 0) {
			JOptionPane.showMessageDialog(null, "La piedra gana");
		}
	}
}
	
	