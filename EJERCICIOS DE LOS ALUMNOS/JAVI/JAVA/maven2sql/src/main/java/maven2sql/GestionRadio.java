package maven2sql;

import java.sql.*;

public class GestionRadio {

    public static void main(String[] args) {
        // 1. Configuración de la conexión
        String url = "jdbc:mysql://localhost:3306/radio_db?serverTimezone=UTC";
        String user = "root";
        String pass = "";

        // 2. Sentencias SQL (Los moldes)
        String sqlInsert = "INSERT INTO emisoras (id, nombre, frecuencia, estilo) VALUES (?, ?, ?, ?)";
        String sqlSelect = "SELECT * FROM emisoras";

        try (Connection conn = DriverManager.getConnection(url, user, pass)) {
            System.out.println("✅ Conexión establecida.");

            // --- FASE 1: INSERCIÓN MASIVA (La lógica de tu Imagen 3 corregida) ---
            // Usamos Object[][] para poder mezclar int y String sin errores
            Object[][] datos = {
                {10, "Los 40", "93.9", "Pop"},
                {11, "Cadena Dial", "91.7", "Pop Español"},
                {12, "RadiOle", "96.9", "Flamenco"},
                {13, "Rock FM", "99.9", "Rock"},
                {14, "Dub FM", "101.1", "Dubstep"},
                {15, "Radio 100", "91.7", "Punk"},
                {16, "Joe FM", "104.1", "Classic"}
            };

            try (PreparedStatement pstmtInsert = conn.prepareStatement(sqlInsert)) {
                for (Object[] fila : datos) {
                    pstmtInsert.setInt(1, (int) fila[0]);      // ID
                    pstmtInsert.setString(2, (String) fila[1]); // Nombre
                    pstmtInsert.setString(3, (String) fila[2]); // Frecuencia
                    pstmtInsert.setString(4, (String) fila[3]); // Estilo
                    pstmtInsert.addBatch(); // Lo añade a la cola de envío
                }
                
                pstmtInsert.executeBatch(); // Envía todo el bloque a MySQL
                System.out.println("✅ Batch ejecutado: 7 emisoras enviadas.");
            }

            // --- FASE 2: LECTURA CON PREPAREDSTATEMENT ---
            System.out.println("\n--- LISTADO DE EMISORAS EN LA BASE DE DATOS ---");
            System.out.printf("%-5s | %-15s | %-10s | %-10s %n", "ID", "NOMBRE", "DIAL", "ESTILO");
            System.out.println("----------------------------------------------------------");

            try (PreparedStatement pstmtSelect = conn.prepareStatement(sqlSelect);
                 ResultSet rs = pstmtSelect.executeQuery()) {

                while (rs.next()) {
                    System.out.printf("%-5d | %-15s | %-10s | %-10s %n", 
                        rs.getInt("id"), 
                        rs.getString("nombre"), 
                        rs.getString("frecuencia"),
                        rs.getString("estilo"));
                }
            }

        } catch (SQLException e) {
            // Si ves el error "Duplicate entry", es que los IDs ya están en MySQL
            System.err.println("❌ Error en el sistema: " + e.getMessage());
        }
    }
}