package tryCatch;

import java.io.*;
import java.util.Arrays;

public class RetoFicheros {
    public static void main(String[] args) {
        // 1. Definición de rutas base
        String rutaBase = "C:\\prueba\\";
        String[] carpetas = {"CLIENTES", "PROVEEDORES", "PRODUCTOS"};
        
        // 2. Definición de los Arrays de datos
        String[] clientes = {"Ayto Málaga", "Erosky", "Carrefour"};
        String[] proveedores = {"Microsoft", "Google", "Apple"};
        String[] productos = {"Office", "Gemini", "Iphone 17 pro"};
        
        // 3. Ejecución del reto
        try {
            System.out.println("--- Iniciando Reto ---");
            
            // Procesar cada categoría
            gestionarCategoria(rutaBase, carpetas[0], "CLIENTES.txt", clientes);
            gestionarCategoria(rutaBase, carpetas[1], "PROVEEDORES.txt", proveedores);
            gestionarCategoria(rutaBase, carpetas[2], "PRODUCTOS.txt", productos);
            
            System.out.println("\n--- Reto Finalizado con Éxito ---");
            
        } catch (IOException e) {
            System.out.println("Error en el proceso: " + e.getMessage());
        }
    }

    /**
     * Método que crea carpeta, crea fichero, escribe array y muestra datos
     */
    public static void gestionarCategoria(String base, String carpeta, String nombreFich, String[] datos) throws IOException {
        // Crear Carpeta
        File dir = new File(base + carpeta);
        if (!dir.exists()) {
            dir.mkdirs();
            System.out.println("Carpeta creada: " + carpeta);
        }

        // Crear y Escribir Fichero
        File archivo = new File(dir, nombreFich);
        try (PrintWriter writer = new PrintWriter(new FileWriter(archivo))) {
            for (String dato : datos) {
                writer.println(dato);
            }
        }
        System.out.println("Fichero escrito: " + nombreFich);

        // Mostrar Datos (Lectura)
        System.out.println("Contenido de " + nombreFich + ":");
        try (BufferedReader reader = new BufferedReader(new FileReader(archivo))) {
            String linea;
            while ((linea = reader.readLine()) != null) {
                System.out.println("  - " + linea);
            }
        }
        System.out.println("-----------------------");
    }
}