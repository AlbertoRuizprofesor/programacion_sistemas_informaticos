package Metodos;

public class MainOperaciones {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Operaciones operaciones = new Operaciones();
		int[] numero = operaciones.pedirDatos();
		operaciones.lista_Operaciones(numero[0], numero[1]);

	}

}
