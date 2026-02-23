package mvc2;

public class Controlador {
	
	private Modelo modelo;
	private Vista vista;
		
	public Controlador(Modelo modelo, Vista vista) {
		
		this.modelo = modelo;
		this.vista = vista;
	}
		
	public void actualizarVista() {
	
	String nombre = modelo.getNombre();
	Double precio = modelo.getPrecio();
	vista.mostrarDatos(nombre, precio);
	
	}
}
	
	
	


