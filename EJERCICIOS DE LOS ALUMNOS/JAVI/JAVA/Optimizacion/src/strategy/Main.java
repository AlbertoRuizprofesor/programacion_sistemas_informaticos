package strategy;

//Ejemplo de uso
public class Main {
	public static void main(String[] args) {

		// Seleccionamos las estrategias de pago
		EstrategiaPago estrategiaTarjeta = new PagoTarjetaCredito("1234 5678 9012 3456", "12/25", "123");

		EstrategiaPago estrategiaPayPal = new PagoPayPal("alberto@correo.com", "12345");

		EstrategiaPago estrategiaBitcoin = new PagoBitcoin("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa");

		// Contexto con la estrategia de pago con tarjeta
		ContextoPago contexto = new ContextoPago(estrategiaTarjeta);
		contexto.pagar(100.0);

		// Cambiamos la estrategia de pago a PayPal
		contexto = new ContextoPago(estrategiaPayPal);
		contexto.pagar(50.0);
		
		// Cambiamos a Bitcon
		contexto = new ContextoPago(estrategiaBitcoin);
		contexto.pagar(250.75);

	}
}
