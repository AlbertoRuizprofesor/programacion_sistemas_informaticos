package ejercicio18;

public class Equipo {
	private String nombreEquipo;
	private Jugador[] jugadores; // Declaramos el array de objetos Jugador

	public Equipo(String nombreEquipo, Jugador[] jugadoresEntrada) {
		this.nombreEquipo = nombreEquipo;
		this.jugadores = jugadoresEntrada;
	}

	public void mostrarPlantilla() {
		System.out.println("EQUIPO: " + nombreEquipo);
		System.out.println("---------------------------");
		// Recorremos el array para mostrar a cada jugador
		for (int i = 0; i < jugadores.length; i++) {
			System.out.println("Jugador " + (i + 1) + ": " + jugadores[i].getInfo());
		}
	}
}