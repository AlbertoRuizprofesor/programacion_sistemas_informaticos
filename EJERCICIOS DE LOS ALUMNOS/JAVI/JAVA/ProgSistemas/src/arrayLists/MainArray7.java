package arrayLists;

import java.util.ArrayList;

public class MainArray7 {

	public static void main(String[] args) {

		var personas = new ArrayList<Array7>();
		
		personas.add(new Array7("Pepe", 23));
		personas.add(new Array7("Alicia", 33));
		personas.add(new Array7("Laura", 13));
		personas.add(new Array7("Nicoleta", 43));
		personas.add(new Array7("Juan", 50));
		
		for (var persona : personas) {
			System.out.println(persona);
		}

	}

}
