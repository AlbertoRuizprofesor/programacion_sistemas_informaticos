package tryCatch;

import java.io.*;
import java.util.ArrayList;

public class WriteFileBytes {
    public static void main(String[] args) {
        File fichero = new File(".\\src\\fileBytes.dat");
        
        // 1. Usamos un ArrayList para almacenar los números antes de escribir
        ArrayList<Integer> listaBytes = new ArrayList<>();
        for (int i = 1; i < 100; i++) {
            listaBytes.add(i);
        }

        // 2. Usamos try-with-resources para asegurar que los flujos se cierren solos
        try (FileOutputStream fileout = new FileOutputStream(fichero, true);
             FileInputStream filein = new FileInputStream(fichero)) {

            // Escribimos el contenido del ArrayList en el fichero
            for (Integer dato : listaBytes) {
                fileout.write(dato);
            }
            
            // Forzamos que se escriban los datos pendientes en el disco
            fileout.flush();

            System.out.println("--- Contenido del fichero ---");
            // 3. Leemos y, si quieres, podemos guardarlo en otro ArrayList o mostrarlo
            int data;
            while ((data = filein.read()) != -1) {
                System.out.println(data);
            }

        } catch (IOException e) {
            System.err.println("Hubo un error al manejar el fichero: " + e.getMessage());
        }
    }
}