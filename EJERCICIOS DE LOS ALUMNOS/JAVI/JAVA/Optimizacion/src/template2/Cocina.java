package template2;

public class Cocina {
	public static void main(String[] args) {
		System.out.println("Preparando pedido 1:");
		Sandwich pedido1 = new SandwichJamon();
		pedido1.prepararSandwich();

		System.out.println("Preparando pedido 2:");
		Sandwich pedido2 = new SandwichVeggie();
		pedido2.prepararSandwich();
	}
}