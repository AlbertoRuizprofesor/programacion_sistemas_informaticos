package mvcDB;

import java.util.ArrayList;

public class Vista {

	public void mostrarDatos(ArrayList<Cliente> listaClientes) {
		System.out.println("----------------------------");

		System.out.println("LISTADO DE CLIENTES ");

		for (Cliente cliente : listaClientes) {

			System.out.println("ID: " + cliente.getId() + " | NIF: " + cliente.getNif() + " | Nombre: "
					+ cliente.getNombre() + " | Edad: " + cliente.getEdad());

		}

		System.out.println("----------------------------");
	}

}
