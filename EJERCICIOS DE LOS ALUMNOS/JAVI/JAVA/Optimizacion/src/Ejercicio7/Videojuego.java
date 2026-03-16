package Ejercicio7;

public class Videojuego {
    private String nombre;
    private int anio;
    private double precio;
    private String plataforma;
    private String sinopsis;
    private String requerimientosMinimos;

    // Constructor que será usado por el Builder
    public Videojuego(String nombre, int anio, double precio, String plataforma, String sinopsis, String requerimientosMinimos) {
        this.nombre = nombre;
        this.anio = anio;
        this.precio = precio;
        this.plataforma = plataforma;
        this.sinopsis = sinopsis;
        this.requerimientosMinimos = requerimientosMinimos;
    }

    public void mostrarFichaTecnica() {
        System.out.println("======= FICHA DEL JUEGO =======");
        System.out.println("Título:       " + nombre + " (" + anio + ")");
        System.out.println("Precio:       " + precio + "€");
        System.out.println("Plataforma:   " + plataforma);
        System.out.println("Sinopsis:     " + sinopsis);
        System.out.println("Requisitos:   " + requerimientosMinimos);
        System.out.println("===============================\n");
    }
}