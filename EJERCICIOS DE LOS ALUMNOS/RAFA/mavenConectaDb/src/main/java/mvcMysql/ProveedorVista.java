package mvcMysql;

import java.util.ArrayList;

public class ProveedorVista {
	public void mostrarProveedor(ArrayList<Proveedor> listaProveedor) {
		System.out.println("LISTADO DE PROVEEDORES");
		for(Proveedor c : listaProveedor) {
			System.out.println(
					"ID: "+ c.getId()
					+ "  |  Nombre: "+ c.getNombre()
					+ "  |  Telefono: "+ c.getTelefono()
					+ "  |  email: "+ c.getEmail()
			);
		}
	}
}
