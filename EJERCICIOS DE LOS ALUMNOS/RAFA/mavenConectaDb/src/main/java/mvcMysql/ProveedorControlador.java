package mvcMysql;

import java.sql.*;
import java.util.ArrayList;

public class ProveedorControlador {

    private Connection conn;
    // Asociación
    private ArrayList<Proveedor> listaProveedor;
    private ClienteVista vista;
    public ProveedorControlador(ProveedorVista vista) {
        this.vista = vista;
        listaProveedor = new ArrayList<>(); //esto es un arraylist

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
    
    
    
    
    
    public void cargarProveedor() {
        try {
            String sql = "SELECT * FROM proveedores";
            PreparedStatement ps = conn.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
            //aqui estamos creando un objeto por cada registro.
            while (rs.next()) {
                Cliente c = new Cliente(
                        rs.getInt("id"),
                        rs.getString("nombre"),
                        rs.getString("telefono"),
                        rs.getString("email")
                );
                //cada objeto nuevo lo añadimos a listaclientes
                listaProveedor.add(c);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void mostrarProveedor() {
        vista.mostrarProveedor(listaProveedor);
    }

}
