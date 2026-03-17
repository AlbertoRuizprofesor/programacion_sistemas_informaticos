package decorator;

public class Main {
	public static void main(String[] args) {
		Mensaje mensaje = new MensajeBasico("MENSAJE PRINCIPAL");

		// Decorar el mensaje con un encabezado
		Mensaje mensajeDecorado = new MensajeConEncabezado(
				new MensajeConPieDePagina(mensaje, "Pie de página."), "Encabezado");

		System.out.println(mensajeDecorado.obtenerContenido());

	}
}
