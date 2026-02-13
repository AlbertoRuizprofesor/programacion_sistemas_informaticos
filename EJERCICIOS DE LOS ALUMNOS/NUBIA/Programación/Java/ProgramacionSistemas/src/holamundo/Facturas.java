package holamundo;

import java.util.Scanner;

public class Facturas {

    public static void main(String[] args) {
        // Creamos el scanner para leer datos
        Scanner sc = new Scanner(System.in);

        System.out.println("--- Sistema de Facturación ---");

        // 1. Entrada de datos
        System.out.print("Introduce el nombre del producto: ");
        String producto = sc.nextLine();

        System.out.print("Introduce el precio unitario: ");
        double precio = sc.nextDouble();

        System.out.print("Introduce la cantidad: ");
        int cantidad = sc.nextInt();

        // 2. Cálculos de la factura
        double subtotal = precio * cantidad;
        double porcentajeIva = 0.21; // Ejemplo: 21% de IVA
        double totalIva = subtotal * porcentajeIva;
        double totalFinal = subtotal + totalIva;

        // 3. Salida de resultados (Formateada)
        System.out.println("\n------- DETALLE DE FACTURA -------");
        System.out.println("Producto:    " + producto);
        System.out.println("Cantidad:    " + cantidad);
        System.out.printf("Subtotal:    $%.2f\n", subtotal);
        System.out.printf("IVA (21%%):   $%.2f\n", totalIva);
        System.out.println("----------------------------------");
        System.out.printf("TOTAL A PAGAR: $%.2f\n", totalFinal);
        System.out.println("----------------------------------");

        // Cerramos el scanner
        sc.close();
    }
}