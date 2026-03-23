package ejercicio18;

public class Jugador {
	private String nombre;
	private int dorsal;

	public Jugador(String nombre, int dorsal) {
		this.nombre = nombre;
		this.dorsal = dorsal;
	}

	public String getInfo() {
		return "Nombre: " + nombre + " (Dorsal: " + dorsal + ")";
	}
}