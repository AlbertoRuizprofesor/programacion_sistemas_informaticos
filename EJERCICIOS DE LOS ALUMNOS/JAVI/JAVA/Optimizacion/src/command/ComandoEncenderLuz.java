package command;

public class ComandoEncenderLuz implements Comando {

	private Luz luz;

	public ComandoEncenderLuz(Luz luz) {
		this.luz = luz;
	}

	@Override
	public void ejecutar() {
		luz.encender();
	}
}
