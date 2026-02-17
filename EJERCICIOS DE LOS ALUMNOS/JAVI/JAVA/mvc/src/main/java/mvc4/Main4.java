package mvc4;

import mvc4.Controlador4;
import mvc4.Vista;

public class Main4 {
        
    public static void main(String[] args) {    	
    	
        // 1. Creamos la Vista
        Vista vista = new Vista();             
        
        // 2. Creamos el Controlador pasándole la vista
        Controlador4 controlador = new Controlador4(vista);             
        
        // 3. Ejecutamos la lógica para cargar y mostrar
        controlador.actualizarVista();        
    }
}