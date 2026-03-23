package ejercicio15;

public class Pelicula {
	private String titulo;
	private String director;
	private int duracion; // en minutos

	// Constructor
	public Pelicula(String titulo, String director, int duracion) {
		this.titulo = titulo;
		this.director = director;
		this.duracion = duracion;
	}

	// Método que devuelve true si dura más de 120 min
	public boolean esLarga() {
		return this.duracion > 120;
	}

	// Método para mostrar la ficha técnica
	public void mostrarInfo() {
		System.out.println("Película: " + titulo);
		System.out.println("Director: " + director);
		System.out.println("Duración: " + duracion + " min");

		// Usamos el método esLarga() para decidir qué imprimir
		if (esLarga()) {
			System.out.println("Nota: Esta es una película de larga duración.");
		} else {
			System.out.println("Nota: Es una película de duración estándar.");
		}
		System.out.println("---------------------------------");
	}
}