package ejercicio7;

public class Main {
	public static void main(String[] args) {
		// Creamos varios animales
		Animal perro = new Animal("Rex", "Perro");
		Animal gato = new Animal("Michi", "Gato");
		Animal leon = new Animal("Simba", "León");

		// Llamamos a sus métodos
		perro.presentarse();
		perro.hacerSonido();

		System.out.println("---");

		gato.presentarse();
		gato.hacerSonido();

		System.out.println("---");

		leon.presentarse();
		leon.hacerSonido();
	}
}