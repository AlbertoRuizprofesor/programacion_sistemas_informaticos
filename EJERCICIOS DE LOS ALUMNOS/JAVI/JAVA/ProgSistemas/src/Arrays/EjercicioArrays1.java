package Arrays;

public class EjercicioArrays1 {

	public static void main(String[] args) {

		int[] array1 = { 1, 34, 56, 67 };

		String[] array2 = { "Albert", "12", "Laura", "17", "Pedro", "10" };

		String[] array3 = new String[5];

		int[] array4 = new int[5];

		String[][] array5 = { { "Albert", "12" }, { "Laura", "17" } };
		
		String[] [] [] array6 = { { { "España", "Madrid" }, { "Italia", "Roma" }}, {{"China", "Pekín"}, {"Japón" , "Tokio"} } };
		
		
		for (int i = 0; i < array6.length; i++) {           	// Nivel 1: Bloques (Continentes)
		    for (int j = 0; j < array6[i].length; j++) {    	// Nivel 2: Filas (Países)
		        for (int k = 0; k < array6[i][j].length; k++) { // Nivel 3: Datos (Nombre/Capital)
		            System.out.print(array6[i][j][k] + " ");
		        }
		        System.out.println(); // Salto de línea tras cada país
		    }
		    System.out.println("----------"); // Separador tras cada bloque
		}
		
		//FOR EACH
		
		/*for (String[][] bloque : array6) {        // Extraemos cada matriz 2D
		    for (String[] fila : bloque) {          // Extraemos cada fila (país)
		        for (String dato : fila) {          // Extraemos cada dato individual
		            System.out.print(dato + " ");
		        }
		        System.out.println();
		    }
		    System.out.println("----------");
		}
		
		
		/* for (String[] fila : array5) {
			for (String columna : fila) {
				System.out.print(columna + " ");
			}
			System.out.println();
		}

		for (int i = 0; i < array5.length; i++) {
			for (int j = 0; j < array5[i].length; j++) {
				System.out.print(array5[i][j] + " ");
			}
			System.out.println(); // Salto de línea al terminar cada fila
		}
		/*
		 * 
		 * System.out.println("array 1 con bucle for"); for (int i = 0; i < 3; i++) {
		 * System.out.println(array1[i]);
		 * 
		 * }
		 * 
		 * // en vez de usar i<3 usaremos length
		 * System.out.println("array 1 con bucle for y length***********"); for (int i =
		 * 0; i < array1.length; i++) { System.out.println(array1[i]);
		 * 
		 * } System.out.println("array 1 con bucle for each************"); // usando
		 * bucles for each for (int y : array1) { System.out.println(y);
		 * 
		 * }
		 */
		/*
		 * // PARSEAR UN ARRAY
		 * System.out.println("array 1 con bucle for y parseo************");
		 * 
		 * int suma = 0; for (int i = 1; i < array2.length; i += 2) {
		 * 
		 * array4[i] = Integer.parseInt(array2[i]); System.out.println("el valor n es "
		 * + array4[i]); suma += array4[i];
		 * 
		 * } System.out.println("la suma es " + suma);
		 * 
		 */

		/*
		 * //FOR EACH System.out.
		 * println("array 3 vacio y añadir datos, luego mostrar datos con bucle for each***"
		 * ); array3[0] = "Hola"; array3[1] = "Mundo";
		 * 
		 * for (String z : array3) { System.out.println(z); }
		 * 
		 * 
		 * 
		 * System.out.println("intentando que no salgan los null********"); int i = 0;
		 * while (array3[i] != null) { System.out.println(array3[i]);
		 * 
		 * i++; }
		 */
	}
}
