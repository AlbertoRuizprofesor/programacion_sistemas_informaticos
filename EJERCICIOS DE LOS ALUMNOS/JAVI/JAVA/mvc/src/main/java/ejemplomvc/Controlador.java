package ejemplomvc;

public class Controlador {
    private Persona modelo;
    private Vista vista;

    // Constructor que recibe ambos objetos
    public Controlador(Persona modelo, Vista vista) {
        this.modelo = modelo;
        this.vista = vista;
    }

    // Método solicitado para orquestar la actualización
    public void actualizarVista() {
        // Extrae el nombre del modelo y se lo pasa al método de la vista
        String nombre = modelo.getNombre();
        String apellidos = modelo.getApellidos();
        vista.mostrarDatos(nombre, apellidos);
    }
}

