package repasoSocket;

public class Ejercicio1 {
    public static void main(String[] args) {

        Thread hilo = new Thread(() -> 
            System.out.println("Hola desde el hilo secundario")
        );

        hilo.start();
    }
}
