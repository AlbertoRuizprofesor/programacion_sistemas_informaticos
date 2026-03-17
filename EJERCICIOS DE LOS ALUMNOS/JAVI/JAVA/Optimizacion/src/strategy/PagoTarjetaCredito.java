package strategy;

// Estrategia de pago con tarjeta de crédito
class PagoTarjetaCredito implements EstrategiaPago {
	private String numeroTarjeta;
	private String fechaCaducidad;
	private String cvv;

	public PagoTarjetaCredito(String numeroTarjeta, String fechaCaducidad, String cvv) {
		this.numeroTarjeta = numeroTarjeta;
		this.fechaCaducidad = fechaCaducidad;
		this.cvv = cvv;
	}

	@Override
	public void pagar(double cantidad) {
		
		System.out.println("Pagando " + cantidad + " € con tarjeta de crédito: " + numeroTarjeta);
	}
}