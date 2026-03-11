package builder;

public class Producto {
    private String nombre;
    private String color;
    private String talla;
    private String fabricante;
    private String modelo;
    private double precio;

    // CORRECCIÓN: El constructor debe recibir TODOS los parámetros del Builder
    public Producto(String nombre, String color, String talla, String fabricante, String modelo, double precio) {
        this.nombre = nombre;
        this.color = color;
        this.talla = talla;
        this.fabricante = fabricante;
        this.modelo = modelo;
        this.precio = precio;
    }

    public void imprimirDetalles() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Precio: " + precio);
        System.out.println("Color: " + color);
        System.out.println("Talla: " + talla);
        System.out.println("Fabricante: " + fabricante);
        System.out.println("Modelo: " + modelo);
    }
}