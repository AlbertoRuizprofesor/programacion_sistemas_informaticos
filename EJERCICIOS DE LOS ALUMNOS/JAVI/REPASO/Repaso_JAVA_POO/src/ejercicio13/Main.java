package ejercicio13;

public class Main {
	public static void main(String[] args) {

		// Creamos un perro de 2 años
		Mascota miMascota = new Mascota("Luna", "Perro", 2);

		// Mostramos su edad inicial
		miMascota.mostrarInfo();

		// Simulamos que pasan dos años
		miMascota.cumplirAnios();
		miMascota.cumplirAnios();

		// Mostramos la información actualizada
		System.out.println("Después de un tiempo...");
		miMascota.mostrarInfo();
	}
}