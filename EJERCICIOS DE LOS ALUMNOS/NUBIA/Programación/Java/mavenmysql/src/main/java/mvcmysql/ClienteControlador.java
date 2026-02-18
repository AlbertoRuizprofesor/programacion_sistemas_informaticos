package mvcmysql;

import java.sql.*;
import java.util.ArrayList;

public class ClienteControlador {
		private ArrayList<Cliente> modelo;
		private ClienteVista vista;
		private Connection conn;
		
		public ClienteControlador(ClienteVista vista) {
			modelo = new ArrayList<>();
			this.vista = vista;
			
			try {
				conn = DriverManager.getConnection("jdbc:mysql://localhost/empresa1", "root", "");
				System.out.println("Conexión establecida");
			}
			catch (SQLException e)  {
				e.printStackTrace();
			}
		}
		public void cargarClientes() {
			try {
				String sql = "SELECT * FROM clientes";
				PreparedStatement ps = conn.prepareStatement(sql);
				ResultSet rs = ps.executeQuery();
				
				while (rs.next()) {
					Cliente c=new Cliente(
							rs.getInt("id"),
							rs.getString("nif"),
							rs.getString("nombre"),
							rs.getString("edad")
							);
					modelo.add(c);
				}
			}
		
				catch (SQLException e) {
					e.printStackTrace(); }
				}
		public void mostrarClientes() {
			vista.mostrarClientes(modelo);
		}
			
}
		

