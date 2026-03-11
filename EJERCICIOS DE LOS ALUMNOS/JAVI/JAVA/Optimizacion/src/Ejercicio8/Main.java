package Ejercicio8;

public class Main {
    public static void main(String[] args) {
        
        // 1. Pizza Barbacoa (Configuración estándar)
        Pizza barbacoa = new PizzaBuilder()
                .tamano("Familiar")
                .masa("Fina")
                .salsa("Barbacoa dulce")
                .ingredientes("Carne picada, bacon, pollo y cebolla")
                .paraCeliacos(false)
                .build();

        // 2. Pizza Andaluza (Para celíacos)
        // Usamos ingredientes típicos: jamón serrano, aceite de oliva, tomate natural
        Pizza andaluza = new PizzaBuilder()
                .tamano("Mediana")
                .salsa("Tomate artesano y Aceite de Oliva")
                .ingredientes("Jamón serrano, aceitunas verdes y queso de cabra")
                .paraCeliacos(true) // Automáticamente ajustará la masa si usamos la lógica del builder
                .build();

        // Imprimir resultados
        System.out.println("PEDIDO 1:");
        barbacoa.mostrarPedido();

        System.out.println("PEDIDO 2:");
        andaluza.mostrarPedido();
    }
}