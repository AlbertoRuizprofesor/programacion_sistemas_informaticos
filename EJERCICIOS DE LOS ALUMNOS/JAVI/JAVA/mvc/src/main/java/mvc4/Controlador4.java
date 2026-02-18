package mvc4;

import java.util.ArrayList;
import java.sql.*;

public class Controlador4 {

    private Connection conn;
    private ArrayList<Productos> listaProductos;
    private Vista vista;

    public Controlador4(Vista vista) {
        this.vista = vista;
        this.listaProductos = new ArrayList<>();
        try {
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/empresa2", "root", "");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void cargarProductos() {
        listaProductos.clear();
        String sql = "SELECT * FROM productos";
        try (PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                // OJO: Si en Cliente el NIF es int, usa rs.getInt("nif")
                Productos c = new Productos(
                    rs.getInt("id"),
                    rs.getString("nombre"),
                    rs.getDouble("precio")
                );
                listaProductos.add(c);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void actualizarVista() {
        cargarProductos(); // Primero traemos los datos de la DB
        vista.mostrarDatos(listaProductos); // Luego se los pasamos a la vista
        
    }
}