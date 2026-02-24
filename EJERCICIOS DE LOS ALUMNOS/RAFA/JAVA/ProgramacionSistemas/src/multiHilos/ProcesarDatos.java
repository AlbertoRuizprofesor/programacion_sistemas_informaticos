package multiHilos;

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