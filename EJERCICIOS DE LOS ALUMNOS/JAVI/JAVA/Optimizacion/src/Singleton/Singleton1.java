package Singleton;

public class Singleton1 {
	private static Singleton1 instance;

	// Constructor privado para evitar la creación de instancias desde fuera de la
	// clase
	private Singleton1() {
	}

	// Método estático para obtener la única instancia de la clase
	public static Singleton1 getInstance() {
		if (instance == null) {
			instance = new Singleton1();
		}
		return instance;
	}

	// Método de ejemplo para mostrar el funcionamiento del Singleton
	public void mostrarMensaje() {
		System.out.println("¡Hola! Soy un Singleton en verdad ave.");
	}

	public static void main(String[] args) {
		// Obtener la instancia del Singleton
		Singleton1 singleton = Singleton1.getInstance();
		Singleton1 singleton1 = Singleton1.getInstance();
		// Usar la instancia para llamar al método showMessage
		singleton.mostrarMensaje();
		singleton1.mostrarMensaje();
		if (singleton1 == singleton) {
			System.out.println("es la misma instancia");
		} else {
			System.out.println("es diferente");
		}

	}
}
