package template2;

public abstract class Sandwich {
    // El "Método Plantilla" que define la secuencia
    public final void prepararSandwich() {
        ponerPan();
        ponerIngredientePrincipal();
        ponerCondimentos();
        cerrarSandwich();
    }

    // Pasos comunes para todos los sándwiches
    public void ponerPan() {
        System.out.println("Poniendo una rebanada de pan en el plato");
    }

    public void cerrarSandwich() {
        System.out.println("Poniendo la segunda rebanada de pan arriba. ¡Listo!");
        System.out.println("-------------------------------------------");
    }

    // Pasos que cada sándwich decide cómo llenar
    abstract void ponerIngredientePrincipal();
    abstract void ponerCondimentos();
}
