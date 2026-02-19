package mvc2;

public class Main {
	public static void main(String[] args) {
		
		Productos producto=new Productos(1, "Portátil", 1200);
		Vista vista=new Vista();
		Controller controlador=new Controller(producto, vista);
		
		controlador.actualizarVista();
		
		
	}

}
