package modelovistacontroladorbasico;

public class Main {

	public static void main(String[] args) {
		Persona modelo = new Persona("Rafa", "Aranda");
		Vista vista = new Vista();
		Controlador controlador=new
					Controlador(modelo,vista);
		controlador.actualizarVista();
		}
}
