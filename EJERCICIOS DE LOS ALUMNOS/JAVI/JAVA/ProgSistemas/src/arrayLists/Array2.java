package arrayLists;

import java.util.ArrayList;

public class Array2 {

	public static void main(String[] args) {
		
		ArrayList<Integer> numeros = new ArrayList<>();
		
		numeros.add(15);
		numeros.add(30);
		numeros.add(68);
		numeros.add(115);
		numeros.add(150);
		numeros.add(95);
		numeros.add(5);
		
		int suma = 0;
		
		for (int num : numeros) {
			suma = suma + num;
		}
		
		System.out.print("Total: " + suma);	

	}

}
