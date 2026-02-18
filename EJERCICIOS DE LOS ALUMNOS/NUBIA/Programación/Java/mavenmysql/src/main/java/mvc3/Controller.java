package mvc3;

public class Controller {
	private Alumnos modelo;
	private Vista vista;
	
	public Controller(Alumnos modelo, Vista vista) {
		this.modelo=modelo;
		this.vista=vista;
	}
	public void actualizarVista() {
		vista.mostrarDatos(modelo.getId(),
				modelo.getNombre(),
				modelo.getApellidos(),
				modelo.getAsignatura(),
				modelo.getNota());
	}

}
