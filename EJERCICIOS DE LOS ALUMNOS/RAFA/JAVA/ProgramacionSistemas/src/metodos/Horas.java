package metodos;

public class Horas {
	public int calculoHoras(int dias) {
		int horas=dias*24;
		return horas;
	}
	public int calculoMinutos(int horas) {
		int minutos=horas*60;
		return minutos;
	}
	public int mostrarDatos(String horas, String minutos) {
		System.out.println(+horas, +minutos);
	}
}
