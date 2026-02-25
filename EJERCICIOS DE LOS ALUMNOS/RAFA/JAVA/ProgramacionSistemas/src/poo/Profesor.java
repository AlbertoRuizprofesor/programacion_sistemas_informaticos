package poo;

public class Profesor extends Persona {
	private String signatura;
	private int salario;

	

	public Profesor(String nombre, String apellidos, int edad, String curso, String asignatura, String signatura, int salario) {
		super(nombre, apellidos, edad);
		this.signatura=signatura;
		this.salario=salario;
		// TODO Auto-generated constructor stub
	}



	public String getsignatura() {
		return signatura;
	}



	public void setsignatura(String asignatura) {
		this.signatura = asignatura;
	}



	public int getSalario() {
		return salario;
	}



	public void setSalario(int salario) {
		this.salario = salario;
	}



	@Override
	public String toString() {
		return "Profesor [signatura=" + signatura + ", salario=" + salario + ", getsignatura()=" + getsignatura()
				+ ", getSalario()=" + getSalario() + ", getNombre()=" + getNombre() + ", getApellidos()="
				+ getApellidos() + ", getEdad()=" + getEdad() + ", toString()=" + super.toString() + ", getClass()="
				+ getClass() + ", hashCode()=" + hashCode() + "]";
	}







	
	
	

}
