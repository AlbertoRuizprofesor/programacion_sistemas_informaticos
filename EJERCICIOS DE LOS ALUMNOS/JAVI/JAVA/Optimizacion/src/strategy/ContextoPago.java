package strategy;

//Contexto que utiliza una estrategia de pago
class ContextoPago {
	private EstrategiaPago estrategiaPago;

	public ContextoPago(EstrategiaPago estrategiaPago) {
		this.estrategiaPago = estrategiaPago;
	}

	public void pagar(double cantidad) {
		estrategiaPago.pagar(cantidad);
	}
}
