package mvc3;

public class Alumnos {

	private int id;
	private String nombre;
	private String apellidos;
	private String asignatura;
	private int nota;

	public Alumnos(int id, String nombre, String apellidos, String asignatura, int nota) {

		this.id = id;
		this.nombre = nombre;
		this.apellidos = apellidos;
		this.asignatura = asignatura;
		this.nota = nota;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

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

	public String getAsignatura() {
		return asignatura;
	}

	public void setAsignatura(String asignatura) {
		this.asignatura = asignatura;
	}

	public int getNota() {
		return nota;
	}

	public void setNota(int nota) {
		this.nota = nota;
	}

}
