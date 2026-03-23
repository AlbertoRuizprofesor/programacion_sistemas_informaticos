package ejercicio6;

public class Main {

	public static void main(String[] args) {
		// Creamos el primer libro
		Libro libro1 = new Libro("Cien años de soledad", "Gabriel García Márquez", 471);

		// Creamos el segundo libro
		Libro libro2 = new Libro("El resplandor", "Stephen King", 599);

		// Mostramos los datos de ambos
		libro1.mostrarInformacion();
		libro2.mostrarInformacion();
	}
}