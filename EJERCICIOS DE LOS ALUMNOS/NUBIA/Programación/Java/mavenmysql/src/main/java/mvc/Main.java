package mvc;

public class Main {
	
	public static void main(String[] args) {
		
		Persona modelo=new Persona("Nubia", "Montesinos", 20);
		Vista vista=new Vista();
		Controller controlador=new Controller(modelo, vista);
		
		controlador.actualizarVista();
	}

}
