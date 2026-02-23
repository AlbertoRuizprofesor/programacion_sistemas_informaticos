package tryCatch;

import java.io.*;

public class ReadFichTexto {
    public static void main(String[] args) {
        // La ruta debe coincidir exactamente con la que usaste para escribir
        File fic = new File("C:\\prueba\\myfile2.txt");

        // Usamos try-with-resources para asegurar el cierre del fichero automáticamente
        try (BufferedReader fichero = new BufferedReader(new FileReader(fic))) {
            
            String linea;
            System.out.println("--- Contenido del archivo leído ---");

            // Leemos línea a línea hasta que se acabe el fichero (null)
            while ((linea = fichero.readLine()) != null) {
                System.out.println(linea);
            }

        } catch (FileNotFoundException e) {
            System.out.println("❌ Error: No se encuentra el fichero en la ruta: " + fic.getAbsolutePath());
        } catch (IOException e) {
            System.out.println("❌ Error de E/S: " + e.getMessage());
        }
    }
}