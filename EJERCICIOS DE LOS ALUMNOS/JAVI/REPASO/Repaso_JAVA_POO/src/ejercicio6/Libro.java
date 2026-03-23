package ejercicio6;

public class Libro {
    // Atributos (características)
    private String titulo;
    private String autor;
    private int numPaginas;

    // Constructor para inicializar el libro
    public Libro(String titulo, String autor, int numPaginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.numPaginas = numPaginas;
    }

    // Método para mostrar toda la información
    public void mostrarInformacion() {
        System.out.println("----- Información del Libro -----");
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Número de páginas: " + numPaginas);
        System.out.println("---------------------------------");
    }
}