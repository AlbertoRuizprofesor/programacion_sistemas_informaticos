package jOption;

import javax.swing.JOptionPane;

public class CalculadoraExpress {
    public static void main(String[] args) {
    
    	String result;
    	int option = JOptionPane.showConfirmDialog(null, "opciones", "opciones en verdad", JOptionPane.ERROR_MESSAGE);
    	
    	if (option == 0) {
    		result = "si";
    	} else {
    		result = "no";
    	}
    	    	
    	
    }   	
    	
}