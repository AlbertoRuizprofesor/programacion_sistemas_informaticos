package state;

public class EstadoSinMoneda implements Estado {
	private MaquinaExpendedora maquinaExpendedora;

	public EstadoSinMoneda(MaquinaExpendedora maquinaExpendedora) {
		this.maquinaExpendedora = maquinaExpendedora;
	}

	@Override
	public void insertarMoneda() {
		System.out.println("Moneda insertada.");
		// Cambiamos el estado de la máquina a "Con Moneda"
		maquinaExpendedora.setEstado(maquinaExpendedora.getEstadoConMoneda());
	}

	@Override
	public void devolverMoneda() {
		System.out.println("No hay moneda para devolver.");
	}

	@Override
	public void presionarBoton() {
		System.out.println("Inserte una moneda primero.");
	}

	@Override
	public void dispensar() {
		System.out.println("Inserte una moneda primero.");
	}
}
