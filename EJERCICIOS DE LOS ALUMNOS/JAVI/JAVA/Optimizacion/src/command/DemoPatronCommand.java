package command;

//Cliente
public class DemoPatronCommand {

	public static void main(String[] args) {

		// Creamos el objeto receptor
		Luz luz = new Luz();

		// Creamos los comandos
		Comando comandoEncender = new ComandoEncenderLuz(luz);
		Comando comandoApagar = new ComandoApagarLuz(luz);

		// Creamos el control remoto
		ControlRemoto control = new ControlRemoto();

		// Encender la luz
		control.setComando(comandoEncender);
		control.presionarBoton();

		// Apagar la luz
		control.setComando(comandoApagar);
		control.presionarBoton();
	}
}
