package ejemplomvc;

public class Main {
    public static void main(String[] args) {
        // 1. Crear el objeto Modelo (Datos)
        Persona persona = new Persona("Carlos", "Martínez Sánchez");

        // 2. Crear el objeto Vista (Interfaz)
        Vista vista = new Vista();

        // 3. Crear el Controlador (Cerebro) inyectando modelo y vista
        Controlador controlador = new Controlador(persona, vista);

        // 4. Invocar el método para ver el resultado
        controlador.actualizarVista();
    }
}