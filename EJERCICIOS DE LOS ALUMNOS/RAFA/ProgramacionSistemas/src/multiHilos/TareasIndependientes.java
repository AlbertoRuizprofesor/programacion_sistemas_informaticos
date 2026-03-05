package multiHilos;

public class TareasIndependientes {
    public static void main(String[] args) {

        Thread hilo1 = new Thread(new DescargarArchivo());
        Thread hilo2 = new Thread(new ProcesarDatos());
        Thread hilo3 = new Thread(new MostrarMensajes());

        hilo1.start();
        hilo2.start();
        hilo3.start();

        System.out.println("Todas las tareas iniciadas");
    }
}
