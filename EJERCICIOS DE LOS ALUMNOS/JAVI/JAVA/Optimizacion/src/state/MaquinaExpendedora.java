package state;

public class MaquinaExpendedora {
	// Definimos los diferentes estados de la máquina
	private Estado estadoSinMoneda;
	private Estado estadoConMoneda;
	private Estado estadoDispensando;

	// Este es el estado actual de la máquina
	private Estado estadoActual;

	// Constructor de la máquina expendedora
	public MaquinaExpendedora() {
		// Inicializamos los estados concretos
		estadoSinMoneda = new EstadoSinMoneda(this);
		estadoConMoneda = new EstadoConMoneda(this);
		estadoDispensando = new EstadoDispensando(this);

		// La máquina empieza sin moneda insertada
		estadoActual = estadoSinMoneda;
	}

	// Método para insertar una moneda
	public void insertarMoneda() {
		estadoActual.insertarMoneda();
	}

	// Método para devolver una moneda
	public void devolverMoneda() {
		estadoActual.devolverMoneda();
	}

	// Método para presionar el botón
	public void presionarBoton() {
		estadoActual.presionarBoton();
		estadoActual.dispensar();
	}

	// Método para cambiar el estado actual de la máquina
	void setEstado(Estado estado) {
		this.estadoActual = estado;
	}

	// Métodos para obtener los estados
	public Estado getEstadoSinMoneda() {
		return estadoSinMoneda;
	}

	public Estado getEstadoConMoneda() {
		return estadoConMoneda;
	}

	public Estado getEstadoDispensando() {
		return estadoDispensando;
	}
}
