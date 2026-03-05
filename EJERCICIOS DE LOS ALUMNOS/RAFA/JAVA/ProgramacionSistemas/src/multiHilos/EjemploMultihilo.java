package multiHilos

class DescargarArchivo implements Runnable {
    @Override
    public void run() {
        System.out.println("Descargando archivo...");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Descarga completa");
    }
}

class ProcesarDatos implements Runnable {
    @Override
    public void run() {
        System.out.println("Procesando datos...");
        try {
            Thread.sleep(1500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Procesamiento terminado");
    }
}

class MostrarMensajes implements Runnable {
    @Override
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("Mensaje " + i);
            try {
                Thread.sleep(700);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class EjemploMultihilo {
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
