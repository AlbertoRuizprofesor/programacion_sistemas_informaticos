package preparedStatement;

// 1. Importaciones necesarias
import java.sql.*;

public class InsertarDatos {
    public static void main(String[] args) {
        String sql = "INSERT INTO proveedores (id, nombre, telefono, email) " +
                     "VALUES (1, 'Darío', '633104292', 'dariovillenarosado@gmail.com')";

        // 2. Usar try-with-resources para auto-cerrar conexión y statement
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/empresa2", "root", "");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            
            int filasAfecatadas = stmt.executeUpdate();
            System.out.println("Datos insertados. Filas afectadas: " + filasAfecatadas);

        } catch (SQLException e) {
            System.out.println("Error en la conexión o SQL: " + e.getMessage());
            e.printStackTrace();
        }
    }
}