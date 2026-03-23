package ejercicio17;

public class Compra {
	private String producto;
	private double precio;

	public Compra(String producto, double precio) {
		this.producto = producto;
		this.precio = precio;
	}

	public void mostrarCompra() {
		System.out.println("--- DETALLES DE COMPRA ---");
		System.out.println("Producto: " + producto);
		System.out.println("Precio: " + precio + "€");
	}
}