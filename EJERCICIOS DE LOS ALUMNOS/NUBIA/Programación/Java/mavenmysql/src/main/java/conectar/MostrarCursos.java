package conectar;
import java.sql.*;

public class MostrarCursos {

	    // Configuración de la conexión (Ajusta según tu base de datos)
	    private static final String URL = "jdbc:mysql://localhost:3306/academia";
	    private static final String USER = "root";
	    private static final String PASS = "";

	    public static void main(String[] args) {
	        
	        // 1. Definir la consulta SQL
	        String sql = "SELECT * FROM cursos";

	        // 2. Usar Try-with-resources para asegurar el cierre de la conexión automáticamente
	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement st = con.prepareStatement(sql);
	             ResultSet rs = st.executeQuery(sql)) {

	        System.out.println("LISTADO DE CURSOS");

	            // 3. Recorrer el ResultSet (Iteración sobre las filas)
	            while (rs.next()) {
	                // Obtención de datos por nombre de columna
	                int id = rs.getInt("id");
	                String nombre = rs.getString("nombre");
	                String profesor = rs.getString("profesor");
	                int horas = rs.getInt("horas");

	                // 4. Mostrar en el formato solicitado
	                System.out.println("id: "+id+"\nnombre: "+nombre+"\nprofesor: "+profesor+"\nhoras: "+horas);
	                System.out.println("--------------------------------------------------------------------------");
	            }

	        } catch (SQLException e) {
	            System.err.println("Error al consultar la base de datos: " + e.getMessage());
	        }
	    }
	}

