package conectar;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class InsertarDatosCursos {
    public static void main(String[] args) {
        String sql = "INSERT INTO cursos (id, nombre, profesor, horas) " +
                     "VALUES (1, 'Programación Sistemas', 'Alberto', '520'), "
                     + "(2, 'POO', 'Alberto', '500'), "
                     + "(3, 'Seguridad Informática', 'Nacho', '350')";

        // 2. Usar try-with-resources para auto-cerrar conexión y statement
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/academia", "root", "");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            
            int filasAfecatadas = stmt.executeUpdate();
            System.out.println("Datos insertados. Filas afectadas: " + filasAfecatadas);

        } catch (SQLException e) {
            System.out.println("Error en la conexión o SQL: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
