package arrayLists;

import java.util.ArrayList;

public class Array3 {
	
	public static void main(String[] args) {
	
	ArrayList <String> colores = new ArrayList<>();
	
	colores.add("Rojo");
	colores.add("Azul");
	colores.add("Verde");
	colores.add("Rosa");
	colores.add("Negro");
	colores.add("Amarillo");
	
	colores.remove("Negro");
	
	System.out.println("Lista de colores: " + colores);
	
	}

}
