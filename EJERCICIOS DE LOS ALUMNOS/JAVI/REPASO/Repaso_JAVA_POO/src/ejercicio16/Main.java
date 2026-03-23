package ejercicio16;

public class Main {
	public static void main(String[] args) {

		// Creamos una guitarra eléctrica Fender de 6 cuerdas
		Guitarra miGuitarra = new Guitarra("Fender", 6, "Eléctrica");

		// Probamos los métodos en orden lógico
		miGuitarra.mostrarInfo();
		miGuitarra.afinar();
		miGuitarra.tocar();

	}
}