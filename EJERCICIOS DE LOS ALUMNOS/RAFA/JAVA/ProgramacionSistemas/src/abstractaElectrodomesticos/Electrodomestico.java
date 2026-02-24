package abstractaElectrodomesticos;

public abstract class Electrodomestico {
	private String color;
	private String peso;
	private String marca;
	private String fabricante;
	private String precio;
	
	public Electrodomestico(String color, String peso, String marca, String fabricante, String precio) {
		super();
		this.color = color;
		this.peso = peso;
		this.marca = marca;
		this.fabricante = fabricante;
		this.precio = precio;
	}
	
	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getPeso() {
		return peso;
	}

	public void setPeso(String peso) {
		this.peso = peso;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getFabricante() {
		return fabricante;
	}

	public void setFabricante(String fabricante) {
		this.fabricante = fabricante;
	}

	public String getPrecio() {
		return precio;
	}

	public void setPrecio(String precio) {
		this.precio = precio;
	}
	

	@Override
	public String toString() {
		return "Electrodomestico [color=" + color + ", peso=" + peso + ", marca=" + marca + ", fabricante=" + fabricante
				+ ", precio=" + precio + "]";
	}

	abstract void encender();
	abstract void apagar();
	abstract void comprar();
	abstract void devolver();
}
