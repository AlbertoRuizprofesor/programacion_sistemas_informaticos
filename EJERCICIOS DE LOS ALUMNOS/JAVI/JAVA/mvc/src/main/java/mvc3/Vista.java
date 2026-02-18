package mvc3;

public class Vista {
	
	public void mostrarDatos(int id, String nombre, String apellidos, String asignatura, int nota) {
		System.out.println("----------------------------");
		System.out.println("Cargando Datos... ");
		
		System.out.println("ID: " + id);
		System.out.println("Nombre: " + nombre);
		System.out.println("Apellidos: " + apellidos);
		System.out.println("Asignatura: " + asignatura);
		System.out.println("Nota: " + nota);
		System.out.println("----------------------------");
	}
}
