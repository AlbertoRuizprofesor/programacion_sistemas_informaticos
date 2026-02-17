package arrayLists;

import java.util.ArrayList;

public class MainArray9 {

	public static void main(String[] args) {
		
		String nombreBuscar = "Luis";
		boolean encontrado = false;

		var alumnos = new ArrayList<Array9>();

		alumnos.add(new Array9("Juan", 25));
		alumnos.add(new Array9("José", 35));
		alumnos.add(new Array9("Ana", 25));
		alumnos.add(new Array9("Juan", 25));

		for (var alumno : alumnos) {
			System.out.println("Alumno: " + alumno);
		}

		for (var alumno : alumnos) {
			if (alumno.getNombre().equals(nombreBuscar)) {
				System.out.println("Nota: " + alumno.getNota());
				encontrado = true;
			}
		}

		if (!encontrado) {
			System.out.println("Alumno no encontrado");
		}

	}
}
