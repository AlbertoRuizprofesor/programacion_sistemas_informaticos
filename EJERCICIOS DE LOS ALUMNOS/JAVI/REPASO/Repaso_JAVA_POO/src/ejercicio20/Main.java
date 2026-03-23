package ejercicio20;

public class Main {
	public static void main(String[] args) {

		// Creamos dos libros
		Libro libro1 = new Libro("El Quijote", "Miguel de Cervantes");
		Libro libro2 = new Libro("1984", "George Orwell");

		// 1. Consultamos estado inicial
		libro1.mostrarEstado();

		// 2. Prestamos el libro 1
		libro1.prestarLibro();

		// 3. Intentamos prestar el libro 1 OTRA VEZ (debería dar error)
		libro1.prestarLibro();

		// 4. Mostramos estados actualizados
		libro1.mostrarEstado();
		libro2.mostrarEstado();

		// 5. Devolvemos el libro 1
		libro1.devolverLibro();
		libro1.mostrarEstado();
	}
}