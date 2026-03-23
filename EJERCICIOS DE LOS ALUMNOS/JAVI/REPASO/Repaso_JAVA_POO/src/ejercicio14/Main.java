package ejercicio14;

public class Main {
	public static void main(String[] args) {

		// Creamos tres ordenadores con distintas potencias
		Ordenador pcOficina = new Ordenador("HP", 8, 500);
		Ordenador pcGaming = new Ordenador("MSI", 32, 2000);
		Ordenador portatil = new Ordenador("Apple", 16, 512);

		// Mostramos los datos de cada uno
		pcOficina.mostrarCaracteristicas();
		pcGaming.mostrarCaracteristicas();
		portatil.mostrarCaracteristicas();
	}
}