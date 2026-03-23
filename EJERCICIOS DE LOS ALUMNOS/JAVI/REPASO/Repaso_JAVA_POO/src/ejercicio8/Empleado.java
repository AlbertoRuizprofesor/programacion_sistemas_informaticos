package ejercicio8;

public class Empleado {
	private String nombre;
	private double sueldoBase;

	// Constructor
	public Empleado(String nombre, double sueldoBase) {
		this.nombre = nombre;
		this.sueldoBase = sueldoBase;
	}

	// Método para calcular el sueldo anual
	public double calcularSueldoAnual() {
		return this.sueldoBase * 12;
	}

	// Método para mostrar la ficha del empleado
	public void mostrarInformacion() {
		System.out.println("Ficha del Empleado:");
		System.out.println("Nombre: " + nombre);
		System.out.println("Sueldo Mensual: " + sueldoBase + "€");
		// Llamamos al método interno para mostrar el cálculo
		System.out.println("Sueldo Anual: " + calcularSueldoAnual() + "€");
		System.out.println("---------------------------");
	}
}