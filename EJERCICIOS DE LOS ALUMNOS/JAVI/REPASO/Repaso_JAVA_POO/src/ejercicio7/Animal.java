package ejercicio7;

public class Animal {
	private String nombre;
	private String tipo;

	// Constructor
	public Animal(String nombre, String tipo) {
		this.nombre = nombre;
		this.tipo = tipo;
	}

	// Método genérico
	public void hacerSonido() {
		System.out.println(nombre + " (el " + tipo + ") está haciendo un sonido...");
	}

	// Método para presentar al animal
	public void presentarse() {
		System.out.println("Soy " + nombre + " y soy un " + tipo + ".");
	}
}