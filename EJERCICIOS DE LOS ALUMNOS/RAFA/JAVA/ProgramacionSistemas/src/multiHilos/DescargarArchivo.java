package multiHilos;

class DescargarArchivo implements Runnable {
    private int tiempo;

    public DescargarArchivo(int tiempo) {
        this.tiempo = tiempo;
    }

    @Override
    public void run() {
        System.out.println("Descargando archivo...");
        try {
            Thread.sleep(tiempo);
        } catch (InterruptedException e) {
            System.out.println("Descarga interrumpida");
        }
        System.out.println("Descarga completa");
    }
}