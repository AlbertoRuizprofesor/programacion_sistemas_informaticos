package ejercicio14;

public class Ordenador {
	private String marca;
	private int memoriaRAM; // En GB
	private int discoDuro; // En GB

	// Constructor
	public Ordenador(String marca, int memoriaRAM, int discoDuro) {
		this.marca = marca;
		this.memoriaRAM = memoriaRAM;
		this.discoDuro = discoDuro;
	}

	// Método para mostrar las características
	public void mostrarCaracteristicas() {
		System.out.println("Especificaciones del Ordenador:");
		System.out.println("Marca: " + marca);
		System.out.println("Memoria RAM: " + memoriaRAM + " GB");
		System.out.println("Disco Duro: " + discoDuro + " GB");
		System.out.println("---------------------------------");
	}
}