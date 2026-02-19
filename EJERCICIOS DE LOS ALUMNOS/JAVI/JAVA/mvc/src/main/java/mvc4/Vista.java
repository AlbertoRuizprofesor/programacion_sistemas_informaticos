package mvc4;

import java.util.ArrayList;

public class Vista {

	public void mostrarDatos(ArrayList<Productos> listaProductos) {
		System.out.println("----------------------------");

		System.out.println("LISTADO DE PRODUCTOS ");

		for (Productos producto : listaProductos) {

			System.out.println("ID: " + producto.getId() + " | Nombre: "
					+ producto.getNombre() + " | Precio: " + producto.getPrecio());

		}

		System.out.println("----------------------------");
	}

}
