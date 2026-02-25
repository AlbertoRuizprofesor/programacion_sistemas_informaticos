package gestiónFicheros;

import java.io.*;

public class BorrarCarpeta {
    public static void main(String[] args) {
        String ruta = "C:\\";
        String carpeta = "Ejercicio1";
        File directorio = new File(ruta + carpeta);
        
        // 1. Primero comprobamos si el directorio existe
        if (directorio.exists()==true) {
            
            // 2. Intentamos borrarlo
            
            if (directorio.delete()) {
                System.out.println("Carpeta borrada correctamente.");
            } else {
                System.out.println("No se pudo borrar. Asegúrate de que la carpeta esté VACÍA.");
            }
            
        } else {
            // 3. Si no existe, no hay nada que borrar
            System.out.println("La carpeta no existe, no se puede borrar.");
        }
    }
}