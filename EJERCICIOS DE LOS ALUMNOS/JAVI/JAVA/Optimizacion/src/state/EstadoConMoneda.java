package state;

public class EstadoConMoneda implements Estado {
	private MaquinaExpendedora maquinaExpendedora;

	public EstadoConMoneda(MaquinaExpendedora maquinaExpendedora) {
		this.maquinaExpendedora = maquinaExpendedora;
	}

	@Override
	public void insertarMoneda() {
		System.out.println("Ya hay una moneda insertada.");
	}

	@Override
	public void devolverMoneda() {
		System.out.println("Moneda devuelta.");
		// Cambiamos el estado de la máquina a "Sin Moneda"
		maquinaExpendedora.setEstado(maquinaExpendedora.getEstadoSinMoneda());
	}

	@Override
	public void presionarBoton() {
		System.out.println("Botón presionado.");
		// Cambiamos el estado de la máquina a "Dispensando"
		maquinaExpendedora.setEstado(maquinaExpendedora.getEstadoDispensando());
	}

	@Override
	public void dispensar() {
		System.out.println("No se ha dispensado ningún artículo.");
	}
}
