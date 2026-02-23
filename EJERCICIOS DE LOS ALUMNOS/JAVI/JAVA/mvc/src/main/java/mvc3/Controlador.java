package mvc3;

public class Controlador {
	
	private Alumnos alumnos;
	private Vista vista;
		
	public Controlador(Alumnos modelo, Vista vista) {
		
		this.alumnos = modelo;
		this.vista = vista;
	}
		
	public void actualizarVista() {
		
		
	int id = alumnos.getId();
	String nombre = alumnos.getNombre();
	String apellidos = alumnos.getApellidos();
	String asignatura = alumnos.getAsignatura();
	int nota = alumnos.getNota();
	vista.mostrarDatos(id, nombre, apellidos, asignatura, nota);
	
	}
}
	
	