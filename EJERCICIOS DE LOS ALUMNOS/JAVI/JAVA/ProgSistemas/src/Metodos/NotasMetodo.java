package Metodos;

public class NotasMetodo {
	/*
	 * Calcula las notas de un alumno, utilizando para ello un método, que te
	 * devuelva la nota según la puntuación obtenida, menor que 4 suspenso, 5
	 * suficientes, 6 bien, 7,8 notable, 9 y 10 sobresaliente.
	 */

	// ATRIBUTOS
	public int num;

	public String calificacion() {

		if (num < 5) {
			return "Suspenso";
		} else if (num < 6) {
			return "Suficiente";
		} else if (num < 8) {
			return "Bien";
		} else if (num < 9) {
			return "Notable";
		} else if (num <= 10) {
			return "Sobresaliente";
		} else {
			return "Nota no válida";
		}

	}

	public void mostrarNota() {
		System.out.println("La calificacion es: " + calificacion());

	}

}
