package gestiónFicheros;

import java.io.*;

public class ARRAY {
    public static void main(String[] args) throws IOException {
        File fichero = new File("C:\\Users\\nubim\\Desktop\\EjerciciosFicheros\\fichero1.txt");

        // flujo de salida binario
        FileOutputStream fileout = new FileOutputStream(fichero, true);

        // Array normal de enteros
        int[] numeros = {10, 20, 30, 40, 50};

        // Escribir los números como bytes
        for (int n : numeros) {
            fileout.write(n); // cada número como un byte
        }

        fileout.close(); // cerrar salida

        // flujo de entrada binario
        FileInputStream filein = new FileInputStream(fichero);

        System.out.println("Contenido del fichero (números):");

        int b;
        while ((b = filein.read()) != -1) { // leemos cada byte hasta el final
            System.out.println(b); // imprime el número del byte
        }

        filein.close(); // cerrar entrada
    }
}