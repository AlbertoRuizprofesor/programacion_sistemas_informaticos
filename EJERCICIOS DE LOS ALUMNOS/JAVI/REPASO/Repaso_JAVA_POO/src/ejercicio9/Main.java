package ejercicio9;

public class Main {
	public static void main(String[] args) {

		// Creamos tres productos diferentes
		Producto p1 = new Producto("Laptop", 799.99, 5);
		Producto p2 = new Producto("Ratón inalámbrico", 19.50, 20);
		Producto p3 = new Producto("Monitor 4K", 299.00, 3);

		// Mostramos la información de cada uno
		p1.mostrarDetalles();
		p2.mostrarDetalles();
		p3.mostrarDetalles();

	}
}