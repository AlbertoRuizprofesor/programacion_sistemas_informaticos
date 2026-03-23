package ejercicio19;

public class Main {
	public static void main(String[] args) {

		// 1. Creamos el objeto Profesor
		Profesor miProfe = new Profesor("Alberto García", "Programación");

		// 2. Creamos el Instituto y le pasamos el objeto 'miProfe'
		Instituto miInsti = new Instituto("I.E.S. Tecnológico", miProfe);

		// 3. Mostramos la información
		miInsti.mostrarInfoCompleta();

	}
}