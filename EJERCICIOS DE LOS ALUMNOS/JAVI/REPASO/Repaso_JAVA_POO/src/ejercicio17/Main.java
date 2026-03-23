package ejercicio17;

public class Main {
	public static void main(String[] args) {

		// Creamos un objeto de la clase Cliente
		Cliente cliente1 = new Cliente("Lucía Fernández", "lucia@email.com");

		// Creamos un objeto de la clase Compra
		Compra compra1 = new Compra("Teclado Mecánico", 85.50);

		// Mostramos la información de ambos
		cliente1.mostrarCliente();
		System.out.println(); // Espacio en blanco para claridad
		compra1.mostrarCompra();

	}
}