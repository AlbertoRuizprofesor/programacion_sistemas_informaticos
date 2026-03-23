package ejercicio9;

public class Producto {
	private String nombre;
	private double precio;
	private int cantidad;

	// Constructor
	public Producto(String nombre, double precio, int cantidad) {
		this.nombre = nombre;
		this.precio = precio;
		this.cantidad = cantidad;
	}

	// Método para calcular el valor total en el almacén
	public double calcularValorTotal() {
		return this.precio * this.cantidad;
	}

	// Método para mostrar los detalles de forma limpia
	public void mostrarDetalles() {
		System.out.println("Producto: " + nombre);
		System.out.println("Precio unitario: " + precio + "€");
		System.out.println("Cantidad en stock: " + cantidad);
		System.out.println("Valor total del inventario: " + calcularValorTotal() + "€");
		System.out.println("---------------------------------");
	}
}