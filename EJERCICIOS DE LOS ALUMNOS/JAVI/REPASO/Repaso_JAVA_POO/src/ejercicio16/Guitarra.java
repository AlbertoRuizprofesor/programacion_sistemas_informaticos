package ejercicio16;

public class Guitarra {
	private String marca;
	private int numCuerdas;
	private String tipo; // "Eléctrica", "Española", "Acústica"

	// Constructor
	public Guitarra(String marca, int numCuerdas, String tipo) {
		this.marca = marca;
		this.numCuerdas = numCuerdas;
		this.tipo = tipo;
	}

	// Método para afinar
	public void afinar() {
		System.out.println("Afinando las " + numCuerdas + " cuerdas de la guitarra " + marca + "...");
		System.out.println("¡Lista para tocar!");
	}

	// Método para tocar
	public void tocar() {
		System.out.println("Tocando una melodía con la guitarra " + tipo + " " + marca + ".");
		System.out.println("¡Suena increíble!");
	}

	// Método opcional para ver los detalles
	public void mostrarInfo() {
		System.out.println("Guitarra: " + marca + " | Tipo: " + tipo + " | Cuerdas: " + numCuerdas);
	}
}