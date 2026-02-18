package conectar;
import java.sql.*;
import java.util.Scanner;
public class EliminarCurso {


	    private static final String URL = "jdbc:mysql://localhost:3306/academia";
	    private static final String USER = "root";
	    private static final String PASS = "";

	    public static void main(String[] args) {
	        Scanner sc = new Scanner(System.in);

	        // 1. Pedir el ID al usuario
	        System.out.print("Introduce el ID del curso que deseas eliminar: ");
	        int idEliminar = sc.nextInt();

	        // 2. Definir la sentencia SQL con parámetro
	        String sql = "DELETE FROM cursos WHERE id = ?";

	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement ps = con.prepareStatement(sql)) {

	            // 3. Asignar el ID al marcador '?'
	            ps.setInt(1, idEliminar);

	            // 4. Ejecutar la eliminación y capturar las filas afectadas
	            int filasAfectadas = ps.executeUpdate();

	            // 5. Mostrar resultado según el número de filas eliminadas
	            if (filasAfectadas > 0) {
	                System.out.println("Éxito: Se ha eliminado el curso con ID " + idEliminar);
	                System.out.println("Total de filas eliminadas: " + filasAfectadas);
	            } else {
	                System.out.println("No se encontró ningún curso con el ID: " + idEliminar);
	            }

	        } catch (SQLException e) {
	            System.err.println("Error al intentar eliminar: " + e.getMessage());
	        }
	    }
	}
