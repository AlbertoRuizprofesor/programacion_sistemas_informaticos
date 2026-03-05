package poo;

public class Alumno extends Persona {
	private String curso;
	private String asignatura;
	
	public Alumno(String nombre, String apellidos, int edad, String curso, String asignatura) {
		super(nombre, apellidos, edad);
		this.curso = curso;
		this.asignatura = asignatura;
		// TODO Auto-generated constructor stub
	}
	public String getCurso() {
		return curso;
	}
	public void setCurso(String curso) {
		this.curso = curso;
	}
	public String getAsignatura() {
		return asignatura;
	}
	public void setAsignatura(String asignatura) {
		this.asignatura = asignatura;
	}
	@Override
	public String toString() {
		return "Alumno "+super.getApellidos()+" "
				+super.getNombre()+" "+super.getEdad()+
				" "+ "curso "+asignatura+ "asignatura";
	
	
	
	}
	
}
