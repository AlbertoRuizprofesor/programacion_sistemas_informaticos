package mvcMysql;
import java.util.ArrayList;

public class ClienteVista {
	public void mostrarClientes(ArrayList<Cliente> listaClientes) {
		System.out.println("LISTADO DE CLIENTES");
		for(Cliente c : listaClientes) {
			System.out.println(
					"ID: "+ c.getId()
					+ "  |  NIF: "+ c.getNif()
					+ "  |  Nombre: "+ c.getNombre()
					+ "  |  Edad: "+ c.getEdad()
			);
		}
	}
}
