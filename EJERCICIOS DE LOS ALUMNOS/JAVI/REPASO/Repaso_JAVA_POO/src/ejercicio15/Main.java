package ejercicio15;

public class Main {
	public static void main(String[] args) {

		// Película corta (menos de 120 min)
		Pelicula p1 = new Pelicula("Toy Story", "John Lasseter", 81);

		// Película larga (más de 120 min)
		Pelicula p2 = new Pelicula("Oppenheimer", "Christopher Nolan", 180);

		// Mostramos la información de ambas
		p1.mostrarInfo();
		p2.mostrarInfo();

		// También podemos usar el método directamente en un IF aquí en el Main
		if (p2.esLarga()) {
			System.out.println("¡Prepara palomitas extra para " + p2.esLarga() + "!");
		}
	}
}