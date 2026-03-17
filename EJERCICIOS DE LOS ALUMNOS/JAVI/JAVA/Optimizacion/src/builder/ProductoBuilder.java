package builder;

public class ProductoBuilder {
	private String nombre;
	private String color;
	private String talla;
	private String fabricante;
	private String modelo;
	private double precio;

	public ProductoBuilder nombre(String nombre) {
		this.nombre = nombre;
		return this;
	}

	public ProductoBuilder color(String color) {
		this.color = color;
		return this;
	}

	public ProductoBuilder talla(String talla) {
		this.talla = talla;
		return this;
	}

	public ProductoBuilder fabricante(String fabricante) {
		this.fabricante = fabricante;
		return this;
	}

	public ProductoBuilder modelo(String modelo) {
		this.modelo = modelo;
		return this;
	}

	public ProductoBuilder precio(double precio) {
		this.precio = precio;
		return this;
	}

	public Producto build() {
		// Aquí llamamos al constructor de Producto con todos los datos recolectados
		return new Producto(nombre, color, talla, fabricante, modelo, precio);
	}
}