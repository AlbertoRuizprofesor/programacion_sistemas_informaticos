package tryCatch;

import java.io.*;

public class writeFichTextoPrint {
	public static void main(String[] args) {
		// 1. Definimos el array con los datos que queremos escribir
		String[] filas = { 
				"Fila número: 1", 
				"Hola Mundo", 
				"Fila número: 3", 
				"Fila número: 4", 
				"Fila número: 5" 
				};

		try {
			// 2. Creamos el PrintWriter.
			// Nota: Asegúrate de que la carpeta C:\prueba existe o cambia la ruta.
			PrintWriter fichero = new PrintWriter(new FileWriter("C:\\prueba\\myfile2.txt"));

			// 3. Recorremos el array para escribir cada elemento en el fichero
			for (int i = 0; i < filas.length; i++) {
				fichero.println(filas[i]); // escribe la línea actual del array
			}

			fichero.close(); // Cerramos para asegurar que se guarde el contenido
			System.out.println("Fichero escrito correctamente con los datos del array.");

		} catch (FileNotFoundException fn) {
			System.out.println("No se encuentra el fichero");
		} catch (IOException io) {
			System.out.println("Error de E/S");
		}
	}
}