package POO;

public class Ejercicio1 {
	
	//ATRIBUTOS
	private String nombre;
	private String apellidos;
	
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getApellidos() {
		return apellidos;
	}

	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}

	public Ejercicio1(String nombre, String apellidos) {
		
		this.nombre = nombre;
		this.apellidos = apellidos;
	}

	@Override
	public String toString() {
		return "Ejercicio1 [nombre = " + nombre + ", apellidos = " + apellidos + "]";
	}
	
	
	
	

}
