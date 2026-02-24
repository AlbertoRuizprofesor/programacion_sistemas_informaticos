package poo;

public class Persona {
	private String name;
	private String apellidos;
	private int edad;
	public Persona(String nombre, String apellidos, int edad) {
		super();
		this.name = nombre;
		this.apellidos = apellidos;
		this.edad = edad;
	}
	public String getNombre() {
		return name;
	}
	public void setNombre(String nombre) {
		this.name = nombre;
	}
	public String getApellidos() {
		return apellidos;
	}
	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}
	public int getEdad() {
		return edad;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
	@Override
	public String toString() {
		return "Persona: " + name + " "  + apellidos + " edad=" + edad;
	}
}
