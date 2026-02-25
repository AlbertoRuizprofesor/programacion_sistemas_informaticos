package primerospasos;

class Hilo1 extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Hilo 1: " + i);
        }
    }
}

class Hilo2 extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Hilo 2: " + i);
        }
    }
}

public class TestHilos {
    public static void main(String[] args) {
        // Crear hilos
        Hilo1 hilo1 = new Hilo1();
        Hilo2 hilo2 = new Hilo2();

        // Iniciar hilos
        hilo1.start();
        hilo2.start();
    }
}