package gestiónFicheros;

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