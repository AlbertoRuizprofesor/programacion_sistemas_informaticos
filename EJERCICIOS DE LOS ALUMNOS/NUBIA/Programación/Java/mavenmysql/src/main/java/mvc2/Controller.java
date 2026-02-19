package mvc2;

public class Controller {
	private Productos modelo;
	private Vista vista;
	
	public Controller(Productos modelo, Vista vista) {
		this.modelo=modelo;
		this.vista=vista;
	}
	public void actualizarVista() {
		vista.mostrarDatos(modelo.getCódigo(), modelo.getNombre(), modelo.getPrecio());
	}

}
