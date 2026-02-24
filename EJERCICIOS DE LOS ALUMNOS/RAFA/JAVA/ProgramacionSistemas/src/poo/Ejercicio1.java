package poo;

public class Ejercicio1 {
	private String nombre;
	private String apellido;
	public Ejercicio1(String nombre, String apellido) {
		super();
		this.nombre = nombre;
		this.apellido = apellido;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getApellido() {
		return apellido;
	}
	public void setApellido(String apellido) {
		this.apellido = apellido;
	}
	@Override
	public String toString() {
		return "Ejercicio1 [nombre=" + nombre + ", apellido=" + apellido + "]";
	}
	
}
