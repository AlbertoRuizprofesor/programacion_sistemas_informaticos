package mvc2;

public class Controlador2 {
	private Productos modelo;
	private Vista2 vista;
	public Controlador2(Productos modelo, Vista2 vista) {
		this.modelo = modelo;
		this.vista = vista;
	}
	public void actualizarVista() {
		vista.mostrarProductos(modelo.getCodigo(),modelo.getNombre(),modelo.getPrecio());
		
	}
}
