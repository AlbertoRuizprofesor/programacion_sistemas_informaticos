package maven2sql;

import java.sql.*;

public class LectorEmisorasPS {

    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/radio_db?serverTimezone=UTC";
        String user = "root";
        String pass = "";

        // Definimos la consulta. Si quisiéramos filtrar, pondríamos un WHERE estilo = ?
        String sqlSelect = "SELECT * FROM emisoras";

        System.out.println("🔍 Iniciando lectura con PreparedStatement...");

        try (Connection conn = DriverManager.getConnection(url, user, pass);
             PreparedStatement pstmt = conn.prepareStatement(sqlSelect);
             ResultSet rs = pstmt.executeQuery()) {

            System.out.println("\n==========================================================");
            System.out.printf("%-5s | %-20s | %-10s | %-15s %n", "ID", "NOMBRE", "DIAL", "ESTILO");
            System.out.println("----------------------------------------------------------");

            while (rs.next()) {
                // Sacamos los datos por el nombre de la columna de la DB
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");
                String frecuencia = rs.getString("frecuencia");
                String estilo = rs.getString("estilo");

                System.out.printf("%-5d | %-20s | %-10s | %-15s %n", id, nombre, frecuencia, estilo);
            }
            System.out.println("==========================================================");

        } catch (SQLException e) {
            System.err.println("❌ Error en la lectura: " + e.getMessage());
        }
    }
}