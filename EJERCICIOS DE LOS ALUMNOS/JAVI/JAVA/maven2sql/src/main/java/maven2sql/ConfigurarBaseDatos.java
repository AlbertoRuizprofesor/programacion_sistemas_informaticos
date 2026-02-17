package maven2sql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class ConfigurarBaseDatos {

    public static void main(String[] args) {
        // CONEXIÓN AL SERVIDOR (Sin especificar base de datos al principio)
        String urlServidor = "jdbc:mysql://localhost:3306/?serverTimezone=UTC";
        String user = "root";
        String pass = "";

        try (Connection conn = DriverManager.getConnection(urlServidor, user, pass);
             Statement stmt = conn.createStatement()) {

            // 1. Crear la Base de Datos
            String sqlCreateDB = "CREATE DATABASE IF NOT EXISTS radio_db";
            stmt.executeUpdate(sqlCreateDB);
            System.out.println("✅ Base de datos 'radio_db' verificada/creada.");

            // 2. Seleccionar la base de datos para crear la tabla
            stmt.execute("USE radio_db");

            // 3. Crear la Tabla
            String sqlCreateTable = "CREATE TABLE IF NOT EXISTS emisoras ("
                    + "id INT PRIMARY KEY, "
                    + "nombre VARCHAR(100), "
                    + "frecuencia VARCHAR(10), "
                    + "estilo VARCHAR(50))";
            
            stmt.executeUpdate(sqlCreateTable);
            System.out.println("✅ Tabla 'emisoras' verificada/creada.");

        } catch (Exception e) {
            System.err.println("❌ Error al configurar: " + e.getMessage());
            e.printStackTrace();
        }
    }
}