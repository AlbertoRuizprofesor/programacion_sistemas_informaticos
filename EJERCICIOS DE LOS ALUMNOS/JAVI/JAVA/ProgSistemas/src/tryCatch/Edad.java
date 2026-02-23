package tryCatch;

public class Edad {
	public static void main(String[] args) {
		int edad = 15;
		try {
			comprobarEdad(edad);
		} catch (EdadInvalidaException e) {
			System.out.println("Error: " + e.getMessage());
		}
	}

	// Método que puede lanzar la excepción
	public static void comprobarEdad(int edad) throws EdadInvalidaException {

		if (edad < 18) {
			throw new EdadInvalidaException("La edad no puede ser menor de 18 años.");
		}
		System.out.println("La edad es válida, se puede realizar la acción.");
	}
}

// Excepción personalizada
class EdadInvalidaException extends Exception {
	public EdadInvalidaException(String mensaje) {
		super(mensaje);
	}
}
