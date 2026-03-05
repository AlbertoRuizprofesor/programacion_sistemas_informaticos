package conectar;

import java.sql.Connection;
import java.sql.DriverManager; // Falta este
import java.sql.PreparedStatement; // Falta este
import java.sql.SQLException; // Falta este

public class CrearTablaCursos {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        
        // Corregimos los paréntesis y la estructura del SQL
        String sql = "CREATE TABLE IF NOT EXISTS cursos ("
                + "id INT PRIMARY KEY, "
                + "nombre VARCHAR(60) NOT NULL, "
                + "profesor VARCHAR(60), "
                + "horas INT)"; 

        try {
            conn = DriverManager.getConnection("jdbc:mysql://localhost/academia", "root", "");
            
            pstmt = conn.prepareStatement(sql);
            // execute() va SIN el String sql dentro porque ya se definió arriba
            pstmt.execute(); 
            
            System.out.println("Tabla 'cursos' creada exitosamente");

        } catch (SQLException e) {
            System.out.println("Error en la conexión o SQL: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // Es mejor cerrar las conexiones aquí para asegurar que ocurra siempre
            try {
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        }
    }
}