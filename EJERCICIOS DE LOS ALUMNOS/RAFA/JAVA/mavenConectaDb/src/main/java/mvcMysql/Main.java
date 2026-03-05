package mvcMysql;

public class Main {

	public static void main(String[] args) {
		ClienteVista vista = new ClienteVista();

        ClienteControlador controlador = new ClienteControlador(vista);

        controlador.cargarClientes();

        controlador.mostrarClientes();
	}

}
