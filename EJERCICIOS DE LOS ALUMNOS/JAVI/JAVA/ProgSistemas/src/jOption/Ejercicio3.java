package jOption;

import javax.swing.JOptionPane;

public class Ejercicio3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String result;

		int option;
		do {
			option = JOptionPane.showConfirmDialog(null, "opciones", "Desea salir?", JOptionPane.ERROR_MESSAGE);

			if (option == 0) {
				result = "si";
				JOptionPane.showMessageDialog(null, "Has pulsado " + result);
				break;
			} else {
				result = "no";
			}

			JOptionPane.showMessageDialog(null, "Has pulsado " + result);
		} while (option != 0);

	}
}


