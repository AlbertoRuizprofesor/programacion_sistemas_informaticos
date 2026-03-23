package ejercicio18;

public class Main {
	public static void main(String[] args) {

		// 1. Creamos 3 objetos Jugador
		Jugador j1 = new Jugador("Casillas", 1);
		Jugador j2 = new Jugador("Raúl", 7);
		Jugador j3 = new Jugador("Zidane", 5);

		// 2. Metemos los jugadores en un array de tamaño 3
		Jugador[] misJugadores = { j1, j2, j3 };

		// 3. Creamos el equipo pasándole el nombre y el array
		Equipo miEquipo = new Equipo("Real Madrid Legends", misJugadores);

		// 4. Mostramos el resultado
		miEquipo.mostrarPlantilla();
	}
}