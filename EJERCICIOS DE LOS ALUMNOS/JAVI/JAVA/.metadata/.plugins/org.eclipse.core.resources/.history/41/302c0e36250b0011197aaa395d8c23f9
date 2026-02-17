package conectarDb;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Proveedores {

    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost/empresa2"; 
        String user = "root";
        String pass = "";

        
        String update = "INSERT INTO proveedores (id, nombre, telefono, email) VALUES "
                      + "(1, 'María', '666777888', 'maria@gmail.com'), "
                      + "(2, 'José', '666666888', 'jose@gmail.com'), "
                      + "(3, 'Juan', '6777778', 'juan@gmail.com'), "
                      + "(4, 'Manuel', '9888999', 'manuel@gmail.com')";

        try (Connection conn = DriverManager.getConnection(url, user, pass);
             Statement stmt = conn.createStatement()) {
            
            int filasAfectadas = stmt.executeUpdate(update);
            System.out.println("Inserción masiva exitosa. Filas añadidas: " + filasAfectadas);

        } catch (SQLException e) {
            System.err.println("Error al insertar datos: " + e.getMessage());
            e.printStackTrace();
        }
    }
}