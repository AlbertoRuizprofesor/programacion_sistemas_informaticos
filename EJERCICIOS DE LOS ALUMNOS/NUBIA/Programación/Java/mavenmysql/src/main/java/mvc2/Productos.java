package mvc2;

public class Productos {
	private int código;
	private String nombre;
	private double precio;
	
	public Productos(int código, String nombre, double precio) {
		this.código=código;
		this.nombre=nombre;
		this.precio=precio;
	}
	
	public int getCódigo() {
		return código;
	}
	
	public String getNombre() {
		return nombre;
	}
	
	public double getPrecio() {
		return precio;
	}

}
