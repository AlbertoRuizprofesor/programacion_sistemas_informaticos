package mvcDB;

import java.util.ArrayList;
import java.sql.*;

public class Controlador {

    private Connection conn;
    private ArrayList<Cliente> listaClientes;
    private Vista vista;

    public Controlador(Vista vista) {
        this.vista = vista;
        this.listaClientes = new ArrayList<>();
        try {
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/empresa2", "root", "");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void cargarClientes() {
        listaClientes.clear();
        String sql = "SELECT * FROM clientes22";
        try (PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                // OJO: Si en Cliente el NIF es int, usa rs.getInt("nif")
                Cliente c = new Cliente(
                    rs.getInt("id"),
                    rs.getInt("nif"), 
                    rs.getString("nombre"),
                    rs.getString("edad")
                );
                listaClientes.add(c);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void actualizarVista() {
        cargarClientes(); // Primero traemos los datos de la DB
        vista.mostrarDatos(listaClientes); // Luego se los pasamos a la vista
        
    }
}