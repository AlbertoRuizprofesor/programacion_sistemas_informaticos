package conectarDb;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet; 
import java.sql.SQLException;
import java.sql.Statement;

public class MostrarDatos {
    
    public static void main(String[] args) {
        
        String url = "jdbc:mysql://localhost/empresa2"; 
        String user = "root";
        String pass = "";

        // Consulta SQL para traer todo de la tabla
        String sql = "SELECT * FROM productos";

        try (Connection conn = DriverManager.getConnection(url, user, pass);
             Statement stmt = conn.createStatement();
             // El ResultSet se cierra automáticamente al terminar el bloque try
             ResultSet rs = stmt.executeQuery(sql)) {
            
            System.out.println("--- LISTADO DE CLIENTES ---");
            System.out.println("ID | NOMBRE | PRECIO");
            System.out.println("---------------------------");

            // El método .next() mueve el cursor a la siguiente fila
            while (rs.next()) {
                // Obtenemos los datos por el nombre de la columna o por su índice
                int id = rs.getInt("id");
                
                String nombre = rs.getString("nombre");
                String precio = rs.getString("precio");
              
                

                System.out.println(id + " | " + nombre + " | " + precio + "  | ");
            }

        } catch (SQLException e) {
            System.err.println("Error al consultar los datos: " + e.getMessage());
            e.printStackTrace();
        }
    }
}