package template2;


public class SandwichJamon extends Sandwich {
    @Override
    void ponerIngredientePrincipal() {
        System.out.println("Agregando rebanadas de jamón de pavo");
    }

    @Override
    void ponerCondimentos() {
        System.out.println("Agregando mayonesa y mostaza");
    }
}



