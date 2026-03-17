package template;

public class Te extends BebidaConCafeina {
	@Override
	void preparar() {
		System.out.println("Remojando el té");
	}

	@Override
	void agregarCondimentos() {
		System.out.println("Agregando limón");
	}
}
