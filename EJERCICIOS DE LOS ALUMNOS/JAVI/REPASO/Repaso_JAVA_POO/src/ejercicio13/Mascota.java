package ejercicio13;

public class Mascota {
	private String nombre;
	private String especie;
	private int edad;

	// Constructor
	public Mascota(String nombre, String especie, int edad) {
		this.nombre = nombre;
		this.especie = especie;
		this.edad = edad;
	}

	// Método para aumentar la edad
	public void cumplirAnios() {
		this.edad++; // Es lo mismo que: this.edad = this.edad + 1;
		System.out.println("¡Felicidades! " + nombre + " ha cumplido un año más.");
	}

	// Método para mostrar la ficha de la mascota
	public void mostrarInfo() {
		System.out.println("Mascota: " + nombre);
		System.out.println("Especie: " + especie);
		System.out.println("Edad actual: " + edad + " años");
		System.out.println("---------------------------");
	}
}