package mvc3;

public class MainAlumnos {
        
    public static void main(String[] args) {
            
        Alumnos alumnos = new Alumnos(1, "Ana", "Paez", "Matematicas", 6);
        Vista vista = new Vista();             
        Controlador controlador = new Controlador(alumnos, vista);             
        controlador.actualizarVista();
        
    }
}