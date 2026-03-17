package strategy;

//Estrategia de pago con PayPal
class PagoPayPal implements EstrategiaPago {
	private String correo;
	private String contrasena;

	public PagoPayPal(String correo, String contrasena) {
		this.correo = correo;
		this.contrasena = contrasena;
	}

	@Override
	public void pagar(double cantidad) {
		System.out.println("Pagando " + cantidad + " € usando PayPal: " + correo);
	}
}
