package ejercicio11;

public class Asignatura {
	// Atributos privados (Encapsulamiento)
	private String nombre;
	private String profesor;
	private int horasSemanales;

	// Constructor
	public Asignatura(String nombre, String profesor, int horasSemanales) {
		this.nombre = nombre;
		this.profesor = profesor;
		this.horasSemanales = horasSemanales;
	}

	// Getters (Para obtener los valores)
	public String getNombre() {
		return nombre;
	}

	public String getProfesor() {
		return profesor;
	}

	public int getHorasSemanales() {
		return horasSemanales;
	}

	// Setters (Para modificar los valores)
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void setProfesor(String profesor) {
		this.profesor = profesor;
	}

	public void setHorasSemanales(int horasSemanales) {
		this.horasSemanales = horasSemanales;
	}

	// Método para mostrar la información
	public void mostrarAsignatura() {
		System.out.println("Asignatura: " + nombre);
		System.out.println("Profesor/a: " + profesor);
		System.out.println("Horas a la semana: " + horasSemanales + "h");
		System.out.println("---------------------------------");
	}
}