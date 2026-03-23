package ejercicio20;

public class Libro {
	private String titulo;
	private String autor;
	private boolean disponible; // true = en la estantería, false = prestado

	// Constructor: al crear un libro nuevo, lo lógico es que esté disponible
	public Libro(String titulo, String autor) {
		this.titulo = titulo;
		this.autor = autor;
		this.disponible = true;
	}

	// Método para prestar el libro
	public void prestarLibro() {
		if (disponible) {
			disponible = false;
			System.out.println("Has tomado prestado: " + titulo);
		} else {
			System.out.println("Lo sentimos, '" + titulo + "' ya está prestado actualmente.");
		}
	}

	// Método para devolver el libro
	public void devolverLibro() {
		if (!disponible) {
			disponible = true;
			System.out.println("Has devuelto: " + titulo + ". ¡Gracias!");
		} else {
			System.out.println("Este libro ya estaba en la biblioteca.");
		}
	}

	// Método para mostrar el estado actual
	public void mostrarEstado() {
		String estado = disponible ? "Disponible" : "Prestado";
		System.out.println("LIBRO: " + titulo + " | Autor: " + autor + " | Estado: [" + estado + "]");
	}
}