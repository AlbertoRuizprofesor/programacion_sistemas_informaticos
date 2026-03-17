package template2;

public class SandwichVeggie extends Sandwich {
	@Override
	void ponerIngredientePrincipal() {
		System.out.println("Agregando láminas de aguacate (palta)");
	}

	@Override
	void ponerCondimentos() {
		System.out.println("Agregando aceite de oliva y sal");
	}
}