package mvc;

public class Controller {
	private Persona modelo;
	private Vista vista;
	
	public Controller(Persona modelo, Vista vista) {
		this.modelo=modelo;
		this.vista=vista;
	}

	public void actualizarVista() {
		vista.mostrarDatos(modelo.getNombre(), modelo.getApellidos(), modelo.getEdad());
	}

	
	
}
