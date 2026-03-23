package ejercicio11;

public class Main {
	public static void main(String[] args) {

		// Creamos la primera asignatura
		Asignatura asig1 = new Asignatura("Programación Java", "Alberto García", 8);

		// Creamos la segunda asignatura
		Asignatura asig2 = new Asignatura("Bases de Datos", "Elena Sanz", 6);

		// Mostramos la información
		asig1.mostrarAsignatura();
		asig2.mostrarAsignatura();

		// Ejemplo de uso de un Setter (cambiamos el profesor de la segunda)
		asig2.setProfesor("Marcos López");
		System.out.println("Actualización realizada:");
		asig2.mostrarAsignatura();
	}
}