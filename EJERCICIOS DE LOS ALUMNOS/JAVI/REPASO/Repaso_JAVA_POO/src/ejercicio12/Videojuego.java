package ejercicio12;

public class Videojuego {
	private String titulo;
	private String plataforma;
	private int horasJugadas;

	// Constructor
	public Videojuego(String titulo, String plataforma, int horasJugadas) {
		this.titulo = titulo;
		this.plataforma = plataforma;
		this.horasJugadas = horasJugadas;
	}

	// Método para añadir horas de sesión al total
	public void jugar(int horasSesion) {
		if (horasSesion > 0) {
			this.horasJugadas += horasSesion;
			System.out.println("Has jugado " + horasSesion + " horas a " + titulo + ".");
		} else {
			System.out.println("Cantidad de horas no válida.");
		}
	}

	// Método para mostrar el progreso
	public void mostrarInformacion() {
		System.out.println("===== BIBLIOTECA DE JUEGOS =====");
		System.out.println("Título: " + titulo);
		System.out.println("Plataforma: " + plataforma);
		System.out.println("Tiempo total: " + horasJugadas + " horas");
		System.out.println("--------------------------------");
	}
}