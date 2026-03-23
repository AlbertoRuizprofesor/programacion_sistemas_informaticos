package ejercicio3;

public class Alumno {

	private String nombre;
	private double nota1;
	private double nota2;

	public Alumno(String nombre, double nota1, double nota2) {

		this.nombre = nombre;
		this.nota1 = nota1;
		this.nota2 = nota2;
	}

	public double CalcularMedia() {

		return (nota1 + nota2) / 2;
	}

}
