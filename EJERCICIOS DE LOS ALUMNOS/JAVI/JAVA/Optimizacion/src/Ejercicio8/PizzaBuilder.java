package Ejercicio8;

public class PizzaBuilder {
    private String tamano;
    private String masa;
    private String salsa;
    private String ingredientes;
    private boolean esCeliaco = false; // Valor por defecto

    public PizzaBuilder tamano(String tamano) {
        this.tamano = tamano;
        return this;
    }

    public PizzaBuilder masa(String masa) {
        this.masa = masa;
        return this;
    }

    public PizzaBuilder salsa(String salsa) {
        this.salsa = salsa;
        return this;
    }

    public PizzaBuilder ingredientes(String ingredientes) {
        this.ingredientes = ingredientes;
        return this;
    }

    public PizzaBuilder paraCeliacos(boolean esCeliaco) {
        this.esCeliaco = esCeliaco;
        // Si es para celiacos, podríamos forzar aquí que la masa sea "Sin Gluten"
        if (esCeliaco) this.masa = "Masa de maíz/arroz (Sin Gluten)";
        return this;
    }

    public Pizza build() {
        return new Pizza(tamano, masa, salsa, ingredientes, esCeliaco);
    }
}