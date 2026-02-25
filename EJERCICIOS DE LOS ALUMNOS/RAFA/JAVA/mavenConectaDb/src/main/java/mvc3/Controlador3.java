package mvc3;

public class Controlador3 {
	private Alumnos modelo;
	private Vista3 vista;
	public Controlador3(Alumnos modelo, Vista3 vista) {
		super();
		this.modelo = modelo;
		this.vista = vista;
	}
	public void actualizarVista() {
		vista.mostrarAlumnos(modelo.getId(),modelo.getNombre(),modelo.getApellidos(),modelo.getAsignatura(),modelo.getNota());
	}
}
