package arrayLists;

import java.util.ArrayList;

public class Ejercicio2 {

	public static void main(String[] args) {

		ArrayList<Integer> numeros = new ArrayList<>();
		
		numeros.add(10);
		numeros.add(20);
		numeros.add(80);
		numeros.add(90);
		numeros.add(120);
		numeros.add(85);
		numeros.add(150);
		numeros.add(12);
		
		// --- Buscar dentro de un ArrayList ---
		// Llamamos al método directamente porque está en la misma clase
		buscar(numeros, 30);

		// --- Reemplazar ---
		modificar1(numeros, 20, 2000); 
		
	} // Cierre del método main

	// Método para buscar
	public static void buscar(ArrayList<Integer> numer, int element) {
		if (numer.contains(element)) {
			System.out.println("Encontrado, la posición es " + numer.indexOf(element));
		} else {
			System.out.println("No encontrado en verdad, tengo hambre");
		}
	}

	// Método para modificar
	public static void modificar1(ArrayList<Integer> numer, int element, int cambiar) {
		if (numer.contains(element)) {
			System.out.println("Encontrado " + element + " modificado con " + cambiar);
			numer.set(numer.indexOf(element), cambiar);
			System.out.println("Lista actualizada: " + numer);
		} else {
			System.out.println("No se puede modificar: el elemento no existe.");
		}
	}


	public static void modificar(ArrayList<Integer> numer, int element, int cambiar) {

		if (numer.contains(element)) {
			System.out.println("encontrado " + element + " modificado con " + cambiar);
			numer.set(numer.indexOf(element), cambiar);
			System.out.println(numer);

		} else {
			System.out.println("no encontrado en verdad, tengo hambre");

		}

	}

}