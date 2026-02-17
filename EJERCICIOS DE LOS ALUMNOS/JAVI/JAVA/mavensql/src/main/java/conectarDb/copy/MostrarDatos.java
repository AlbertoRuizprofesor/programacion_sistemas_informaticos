package conectarDb.copy;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement; // Cambiado de Statement
import java.sql.ResultSet;
import java.sql.SQLException;

public class MostrarDatos {

    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost/empresa2";
        String user = "root";
        String pass = "";

        // Consulta SQL
        String sql = "SELECT * FROM productos";

        // Usamos try-with-resources para manejar la conexión, el pstmt y el rs
        try (Connection conn = DriverManager.getConnection(url, user, pass);
             PreparedStatement pstmt = conn.prepareStatement(sql); // Preparamos la sentencia
             ResultSet rs = pstmt.executeQuery()) { // Ejecutamos sin pasar el string de nuevo

            System.out.println("--- LISTADO DE PRODUCTOS ---");
            System.out.println("ID | NOMBRE | PRECIO");
            System.out.println("---------------------------");

            // Iteramos sobre los resultados
            while (rs.next()) {
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");
                String precio = rs.getString("precio");

                System.out.println(id + " | " + nombre + " | " + precio);
            }

        } catch (SQLException e) {
            System.err.println("Error al consultar los datos: " + e.getMessage());
            e.printStackTrace();
        }
    }
}