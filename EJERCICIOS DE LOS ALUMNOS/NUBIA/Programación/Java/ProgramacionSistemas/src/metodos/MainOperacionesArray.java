package metodos;

public class MainOperacionesArray {
	public static void main(String[] args) {

		Operaciones operaciones=new Operaciones();
		int [] numero=operaciones.pedirDatos();
		operaciones.listaOperaciones(numero[0],numero[1]);
	}
}
