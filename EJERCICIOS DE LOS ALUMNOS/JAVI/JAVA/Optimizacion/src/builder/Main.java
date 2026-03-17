package builder;

public class Main {
    public static void main(String[] args) {
        // Usando el Builder para construir un Producto
        Producto producto = new ProductoBuilder()
                                .nombre("Camiseta")
                                .color("Azul")
                                .talla("M")
                                .fabricante("Zara")
                                .modelo("Navy")
                                .precio(20.0)
                                .build();

        // Imprimir detalles del producto
        producto.imprimirDetalles();
    }
}
