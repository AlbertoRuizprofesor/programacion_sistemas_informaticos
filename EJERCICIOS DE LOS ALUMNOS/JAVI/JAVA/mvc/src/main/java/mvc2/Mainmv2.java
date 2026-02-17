package mvc2;

public class Mainmv2 {
        
    public static void main(String[] args) {
            
        Modelo modelo = new Modelo("Samsung", 230.50);
        Vista vista = new Vista();             
        Controlador controlador = new Controlador(modelo, vista);             
        controlador.actualizarVista();
        
    }
}