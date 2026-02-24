

package mvcMysql;

import java.sql.*;
import java.util.ArrayList;

public class ClienteControlador {

    private Connection conn;
    // Asociación
    private ArrayList<Cliente> listaClientes;
    private ClienteVista vista;
    public ClienteControlador(ClienteVista vista) {
        this.vista = vista;
        listaClientes = new ArrayList<>(); //esto es un arraylist

        try {
            conn = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/empresa1",
                    "root",
                    "");
            System.out.println("Conexión correcta");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    
    
    
    
    public void cargarClientes() {
        try {
            String sql = "SELECT * FROM clientes";
            PreparedStatement ps = conn.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            //aqui estamos creando un objeto por cada registro.
            while (rs.next()) {
                Cliente c = new Cliente(
                        rs.getInt("id"),
                        rs.getString("nif"),
                        rs.getString("nombre"),
                        rs.getString("edad")
                );
                //cada objeto nuevo lo añadimos a listaclientes
                listaClientes.add(c);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void mostrarClientes() {
        vista.mostrarClientes(listaClientes);
    }

}
