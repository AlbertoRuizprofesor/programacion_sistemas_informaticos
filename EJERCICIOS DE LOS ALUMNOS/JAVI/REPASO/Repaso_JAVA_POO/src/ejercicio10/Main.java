package ejercicio10;

public class Main {
	public static void main(String[] args) {

		Movil miMovil = new Movil("Samsung", "S23", 80);

		miMovil.mostrarEstado();

		// Intentamos cargar demasiado
		System.out.println("Intentando cargar un 50% extra...");
		miMovil.cargarBateria(50);

		// Intentamos gastar más de lo que hay
		System.out.println("Usando aplicaciones pesadas (gasto 120%)...");
		miMovil.usarBateria(120);

		miMovil.mostrarEstado();
	}
}