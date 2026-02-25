package jOpcionPanel;

import javax.swing.JOptionPane;

public class Ejercicio2 {

    public static void main(String[] args) {
    	String result;
    	
    	int option=JOptionPane.showConfirmDialog(null,"opciones","desea salir?", JOptionPane.ERROR_MESSAGE);
    	
    	if(option==0) {
    		result="si";
    		JOptionPane.showMessageDialog(null, "has pulsado "+result);
    	}else {
    		result="no";
    	}
    	JOptionPane.showMessageDialog(null, "has pulsado "+result);
         
         
    }
}

