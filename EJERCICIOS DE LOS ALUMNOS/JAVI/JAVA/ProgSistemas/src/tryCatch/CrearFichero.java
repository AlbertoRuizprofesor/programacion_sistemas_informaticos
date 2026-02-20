package tryCatch;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class CrearFichero {
    public static void main(String[] args) {
        // 1. Definimos la ruta del archivo
        Path ruta = Paths.get("c:\\prueba\\mi_nuevo_fichero.txt");

        try {
            // 2. Intentamos crear el archivo
            if (Files.notExists(ruta)) {
                Files.createFile(ruta);
                System.out.println("✅ ¡Archivo creado con éxito!: " + ruta.getFileName());
            } else {
                System.out.println("⚠️ El archivo ya existe.");
            }
        } catch (IOException e) {
            System.err.println("❌ Error al crear el archivo: " + e.getMessage());
        }
    }
}