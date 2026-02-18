package mvc3;

public class Main {
public static void main(String[] args) {
		
		Alumnos modelo=new Alumnos(1, "Nubia", "Montesinos", "Programación", 10);
		Vista vista=new Vista();
		Controller controlador=new Controller(modelo, vista);
		
		controlador.actualizarVista();
	}
}
