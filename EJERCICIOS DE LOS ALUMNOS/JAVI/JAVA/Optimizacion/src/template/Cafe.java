package template;

public class Cafe extends BebidaConCafeina {
	@Override
	void preparar() {
		System.out.println("Filtrando el café");
	}

	@Override
	void agregarCondimentos() {
		System.out.println("Agregando azúcar y leche");
	}
}
