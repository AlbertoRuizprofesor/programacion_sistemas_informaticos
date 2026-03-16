package Ejercicio8;

public class Pizza {
    private String tamano;
    private String masa;
    private String salsa;
    private String ingredientes;
    private boolean esCeliaco;

    // Constructor que usa el Builder
    public Pizza(String tamano, String masa, String salsa, String ingredientes, boolean esCeliaco) {
        this.tamano = tamano;
        this.masa = masa;
        this.salsa = salsa;
        this.ingredientes = ingredientes;
        this.esCeliaco = esCeliaco;
    }

    public void mostrarPedido() {
        System.out.println("--- Tu Pedido de Pizza ---");
        System.out.println("Tamaño:      " + tamano);
        System.out.println("Masa:        " + masa);
        System.out.println("Salsa:       " + (salsa != null ? salsa : "Sin salsa"));
        System.out.println("Ingredientes: " + ingredientes);
        System.out.println("Apta Celiaco: " + (esCeliaco ? "SÍ (Sin Gluten)" : "No"));
        System.out.println("--------------------------\n");
    }
}