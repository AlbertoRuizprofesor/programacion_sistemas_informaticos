package POOAbs;

public abstract class Electrodoméstico {
	private String color;
	private double peso;
	private String marca;
	private String fabricante;
	private double precio;
	
	public Electrodoméstico(String color, double peso, String marca, String fabricante, double precio) {
		this.color=color;
		this.peso=peso;
		this.marca=marca;
		this.fabricante=fabricante;
		this.precio=precio;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color=color;
	}
	public double getPeso() {
		return peso;
	}
	public void setPeso(double peso) {
		this.peso=peso;
	}
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca=marca;
	}
	public String getFabricante() {
		return fabricante;
	}
	public void setFabricante(String fabricante) {
		this.fabricante=fabricante;
	}
	public double getPrecio() {
		return precio;
	}
	public void setPrecio(double precio) {
		this.precio=precio;
	}
	public abstract void encender();
	public abstract void apagar();
	public abstract void comprar();
	public abstract void devolver();

	@Override
	public String toString() {
		return "Electrodoméstico: color="+color+""
				+ ", precio="+precio+", marca="+marca+", fabricante="+fabricante+", precio="+precio;
	}
}
