package ejercicio19;

public class Profesor {
	private String nombre;
	private String modulo; // El nombre de la asignatura

	public Profesor(String nombre, String modulo) {
		this.nombre = nombre;
		this.modulo = modulo;
	}

	// Método para devolver los datos formateados
	public String obtenerDatos() {
		return "Prof. " + nombre + " (Módulo: " + modulo + ")";
	}
}