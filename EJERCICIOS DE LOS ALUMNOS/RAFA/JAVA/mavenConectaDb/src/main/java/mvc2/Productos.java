package mvc2;

public class Productos {
	private int codigo;
	private String nombre;
	private double precio;
	public Productos(int codigo, String nombre, double precio) {
		this.codigo = codigo;
		this.nombre = nombre;
		this.precio = precio;
	}
	public int getCodigo() {
		return codigo;
	}
	
	public String getNombre() {
		return nombre;
	}
	
	public Double getPrecio() {
		return precio;
	}
	
}
