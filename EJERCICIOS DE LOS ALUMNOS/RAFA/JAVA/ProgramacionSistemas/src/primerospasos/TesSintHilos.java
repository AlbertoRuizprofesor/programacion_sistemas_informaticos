package primerospasos;

// Hilo1 sin Thread
class Hilo1 {
    public void ejecutar() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Hilo 1: " + i);
        }
    }
}

// Hilo2 sin Thread
class Hilo2 {
    public void ejecutar() {
        for (int i = 0; i < 5; i++) {
            System.out.println("Hilo 2: " + i);
        }
    }
}

public class TesSintHilos {
    public static void main(String[] args) {
        // Crear objetos
        Hilo1 hilo1 = new Hilo1();
        Hilo2 hilo2 = new Hilo2();

        // Ejecutar secuencialmente
        hilo1.ejecutar();
        hilo2.ejecutar();
    }
}