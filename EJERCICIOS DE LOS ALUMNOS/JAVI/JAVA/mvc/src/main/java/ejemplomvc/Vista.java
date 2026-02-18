package ejemplomvc;

public class Vista {
    // Método que recibe el dato puro y lo formatea para el usuario
    public void mostrarDatos(String nombrePersona, String apellidosPersona) {
        System.out.println("----------------------------");
        System.out.println("Visualizando Datos...");
        System.out.println("Nombre de la persona: " + nombrePersona);
        System.out.println("Apellidos de la persona: " + apellidosPersona);
        System.out.println("----------------------------");
    }
}


