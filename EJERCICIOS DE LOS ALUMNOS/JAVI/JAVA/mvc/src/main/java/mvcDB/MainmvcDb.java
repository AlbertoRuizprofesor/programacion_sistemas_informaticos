package mvcDB;

public class MainmvcDb {
        
    public static void main(String[] args) {
        // 1. Creamos la Vista
        Vista vista = new Vista();             
        
        // 2. Creamos el Controlador pasándole la vista
        Controlador controlador = new Controlador(vista);             
        
        // 3. Ejecutamos la lógica para cargar y mostrar
        controlador.actualizarVista();        
    }
}